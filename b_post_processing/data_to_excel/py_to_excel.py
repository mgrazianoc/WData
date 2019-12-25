import subprocess

name = "x.json"

subprocess.run(f"Rscript to_excel.R -f {name} -s 1 -e 30 -n testing.xlsx -p Data ", shell=True)