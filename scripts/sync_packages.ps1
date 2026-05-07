$ErrorActionPreference = "Stop"

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$dist = Join-Path $root "dist-data"
$pyData = Join-Path $root "python-pkg\src\city_macro_data\data"
$rData = Join-Path $root "r-pkg\inst\extdata"

$requiredFiles = @("city_macro.csv", "metadata.json")
foreach ($f in $requiredFiles) {
  $full = Join-Path $dist $f
  if (-not (Test-Path $full)) {
    throw "Missing file in dist-data: $f"
  }
}

New-Item -ItemType Directory -Force $pyData | Out-Null
New-Item -ItemType Directory -Force $rData | Out-Null

Copy-Item (Join-Path $dist "city_macro.csv") (Join-Path $pyData "city_macro.csv") -Force
Copy-Item (Join-Path $dist "metadata.json") (Join-Path $pyData "metadata.json") -Force
Copy-Item (Join-Path $dist "city_macro.csv") (Join-Path $rData "city_macro.csv") -Force
Copy-Item (Join-Path $dist "metadata.json") (Join-Path $rData "metadata.json") -Force

Write-Host "Synced dist-data to Python and R packages."
