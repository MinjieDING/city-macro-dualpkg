#' Load city macro data
#' @export
load_data <- function() {
  p <- system.file("extdata", "city_macro.csv", package = "citymacrodata")
  utils::read.csv(p, stringsAsFactors = FALSE)
}

#' Read metadata
#' @export
get_metadata <- function() {
  p <- system.file("extdata", "metadata.json", package = "citymacrodata")
  jsonlite::fromJSON(p)
}

#' Return dataset version
#' @export
data_version <- function() {
  get_metadata()$data_version
}

#' Validate dataset basics
#' @param required_columns Character vector of required columns.
#' @export
validate_data <- function(required_columns = c("年份", "城市")) {
  df <- load_data()
  if (nrow(df) == 0) {
    stop("Dataset is empty.", call. = FALSE)
  }

  missing <- setdiff(required_columns, names(df))
  if (length(missing) > 0) {
    stop(
      paste0("Missing required columns: ", paste(missing, collapse = ", ")),
      call. = FALSE
    )
  }
  TRUE
}
