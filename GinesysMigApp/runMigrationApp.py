import subprocess
import os

print(os.getcwd())
os.chdir('..')
main_path= os.path.join(os.path.join(os.path.join(os.getcwd(),'app'),'scripts'), 'main.py')
#method 1
# with open(main_path) as file:
#     exec(file.read())
#method 2
subprocess.run(['python',main_path],capture_output=True,text=True)