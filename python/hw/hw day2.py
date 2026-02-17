python_info = '''Python is simple but very powerful.
It is easy to understand.
Learning python do not require much skills  '''

len_str = len(python_info)
print(len_str)
print(python_info[0], ',' ,python_info[-1].upper())

print(python_info[0:51])

python_info = python_info.replace('Python', 'PYTHON')

python_info = python_info.lower().strip()

new_list = python_info.split()
print(new_list,'\n')

print("course" in python_info)

print("\nThe course description is {} characters long and has {} words.\n".format(len_str, len(new_list)))