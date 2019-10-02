import os 

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
print(current_dir)
print(file_path)
print(os.getcwd())
