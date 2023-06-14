import subprocess,os
current_dir = os.path.dirname(os.path.abspath(__file__))
# List of files in the desired order
scrap=os.path.join(current_dir,"main_codes\\scrapper.py")
clean=os.path.join(current_dir,"main_codes\\cleanup.py")
explore=os.path.join(current_dir,"main_codes\\problem_explorer.py")
prep=os.path.join(current_dir,"TF_IDF_CODES\\prepare.py")
query=os.path.join(current_dir,"TF_IDF_CODES\\query.py")
file_order = [scrap,clean,explore,prep,query]

# Iterate over the files and run each one in order
for file in file_order:
    subprocess.run(["python", file])
    break
