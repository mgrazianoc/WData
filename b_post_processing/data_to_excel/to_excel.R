library("xlsx", "jsonlite", "argparse")

set_enviroment <- function(dirct){
  if (getwd() != dirct){
    print("Setting up directory workspace for R script...")
    setwd(dirct)
  }
}

load_json_file <- function(path){
  print("Loading data from json file...")
  file = jsonlite::fromJSON(path)
  return (file)
}


create_sample <- function(data_frame, starting, ending){
  print("Creating sample from data_set...")
  # cut the unecessary data
  
  print("Creating data frame from sample")
  data_frame = jsonlite::fromJSON(data_frame)
  
  return(data_frame)
}


write_excel_file <- function(final_data, name, sheet_name){
  print("Importing and writting data sample to Excel file...")
  write.xlsx(
    x = final_data,
    file = name,
    sheetName = sheet_name,
    row.names = FALSE
  )
}


parser <- ArgumentParser(description="Creating sample to Excel visualization")
parser$add_argument(
  "file_name", "-f",
  help="selects the directory and file which will be creat the xlsx sample from",
  type="string",
  nargs=1
)
parser$add_argument(
  "--start_index", "-s",
  help="the sample from file data must have a starting index point. Default = 0",
  type="integer",
  nargs=1,
  default=0
)
parser$add_argument(
  "end_index", "-e",
  help="the sample from file data must have a ending index point. Must specify one",
  type="integer",
  narg=1
)
parser$add_argument(
  "--output_excel", "-oe",
  help="optional output for where to save the excel sample",
  type="string",
  nargs=1,
  default="/output"
)
parser$add_argument(
  "--name_excel", "-ne",
  help="optional name which excel data will be save",
  type="string",
  nargs=1,
  default="testing.xlsx"
)
parser$add_argument(
  "sheet_name", "-sn",
  help="the name which will be add to the sheet page",
  type="string",
  nargs=1
)

args <- argparse::ArgumentParser()
set_enviroment()
data_json <- load_json_file(args$file_name)
data_sample <- create_sample(data_json, args$start_index, args$end_index)
write_excel_file(data_sample, args$name_excel, args$sheet_name)