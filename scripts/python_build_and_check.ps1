$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$pkgDir = Join-Path $root "python-pkg"
$distDir = Join-Path $pkgDir "dist"

Write-Host "Installing build tools..."
python -m pip install --upgrade build twine
if ($LASTEXITCODE -ne 0) { throw "Failed to install build tools." }

if (Test-Path $distDir) {
  Write-Host "Cleaning existing dist directory..."
  Remove-Item -Recurse -Force $distDir
}

Write-Host "Building Python package..."
python -m build $pkgDir
if ($LASTEXITCODE -ne 0) { throw "Build failed." }

Write-Host "Running twine check..."
$dists = Get-ChildItem $distDir -File | ForEach-Object { $_.FullName }
python -m twine check $dists
if ($LASTEXITCODE -ne 0) { throw "Twine check failed." }

Write-Host "Build + twine check completed."
