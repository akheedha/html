webdevelopment = ['appu' , 'kichu', 'sachu']
ui_ux_design = ['ram', 'tara', 'raj']
data_science = ['arsha', 'jacky', 'kattappa']

all_participants = [webdevelopment, ui_ux_design, data_science]
print(all_participants)

webdevelopment.append('baabubali')
print(webdevelopment)

data_science.insert(1,'siva')
print(data_science)

ui_ux_design.pop()
print(ui_ux_design)

data_science_new = data_science.copy()
data_science.clear()
print(data_science_new)

print(webdevelopment[:2])

name_len_list = [len(i) for i in data_science_new]
print(name_len_list)

print(f"Is arsha enrolled: {'arsha' in webdevelopment or 'arsha' in ui_ux_design or 'arsha' in data_science_new}")

name_tuple = []
name_tuple.extend([webdevelopment[:1], ui_ux_design[0:1], data_science_new[:1]])
name_tuple = tuple(name_tuple)
print(name_tuple)