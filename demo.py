import os
print(os.getcwd())
print(os.path.join(os.getcwd(),'PreviousVersions'))
os.remove(os.path.join(os.getcwd(),'app.txt'))