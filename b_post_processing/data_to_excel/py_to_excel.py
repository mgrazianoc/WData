import subprocess

def write_to_excel(**kwargs)
    file_name = kwargs.get("file_name")
    start_index = kwargs.get("start_index")
    end_index = kwargs.get("end_index")
    excel_name = kwargs.get("excel_name")
    sheet_name = kwargs.get("sheet_name")
    output_dir = kwargs.get("output_dir")
    
    print("Creating Excel file")
    
    subprocess.run(
        f"Rscript to_excel.R -f {file_name} -s {start_index} -e {end_index} -n {excel_name} -p {sheet_name} ", shell=True)