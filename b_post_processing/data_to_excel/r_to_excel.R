library("openxlsx", "jsonlite", "optparse")

set_enviroment <- function(dirct){
  if (getwd() != dirct){
    print("Setting up directory workspace for R script")
    setwd(dirct)
  }
}

load_json_file <- function(path){
  print("Loading data from JSON file")
  file = jsonlite::fromJSON(path)
  return (file)
}


create_data_frame <- function(data){
  print("Creating data frame from JSON file")
  data <- as.data.frame(data)
  return(data)
}


create_sample <- function(data_frame, starting, ending){
  print("Creating sample from data_set")
  data_frame <- data_frame[c(starting: ending), ]
  return(data_frame)
}


write_excel_file <- function(final_data, name, sheet_name){
  print("Importing and writting data sample to Excel file")
  openxlsx::write.xlsx(
    final_data,
    file = name,
    sheetName = sheet_name,
    firstRow = TRUE, # freezes the first row
    colWidths = "auto",
    creator = "Marco"
  )
}

input_list <- list(

  optparse::make_option(
    c("--file_name", "-f"),
    type="character",
    help="selects the directory and file which will be created the xlsx sample from"
  ),
  
  optparse::make_option(
    c("--start_index", "-s"),
    type="integer",
    help="the sample from file data must have a starting index number"
  ),
  
  optparse::make_option(
    c("--end_index", "-e"),
    type="integer",
    help="the sample from file data must have a ending index point. Must specify one"
  ),
  
  optparse::make_option(
    c("--output", "-o"),
    type="character",
    help="optional output for where to save the excel sample",
    default="/output"
  ),
  
  optparse::make_option(
    c("--name", "-n"),
    help="optional name which excel data will be save"
  ),
  
  optparse::make_option(
    c("--sheet_name", "-p"),
    help="the name which will be add to the sheet page"
  )

)

parser <- optparse::OptionParser(
  option_list = input_list,
  description = "Creating sample to Excel visualization"
  )

args <- optparse::parse_args(parser)

print("Passing command-line values")

set_enviroment("C:/Users/maruc/OneDrive/Área de Trabalho/WData/b_post_processing/data_to_excel")

data_json <- load_json_file(args$file_name)
data_frame <- create_data_frame(data_json)
data_sample <- create_sample(data_frame, args$start_index, args$end_index)
write_excel_file(data_sample, args$name, args$sheet_name)













