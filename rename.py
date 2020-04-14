import os
os.chdir(r"C:\Users\singh\Desktop\rename us")

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split(" ")
    
    new_name = "{}-{}{}".format(f_num, f_title, f_ext)

    os.rename(f, new_name)