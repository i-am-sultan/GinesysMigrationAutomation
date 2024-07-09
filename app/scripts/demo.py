import os
print(os.getcwd())
print(os.path.join(os.getcwd(),'PreviousVersions'))
print(os.path.join(os.getcwd(),'version.txt'))
# os.remove(os.path.join(os.getcwd(),'app.txt'))
latest_version ='v0.0.1'
update_dir_name = f"MigrationAutomation_{latest_version}"
update_dir_path = os.path.join(os.getcwd(), update_dir_name)
print(update_dir_path)
# current_filename = os.path.join(os.getcwd(),os.path.basename(update_url))
os.chdir("..")
print(os.getcwd())
# print(parent_dir)
print(os.path.join(os.getcwd(),'PreviousVersions'))