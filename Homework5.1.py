#_ => True
#__ => False
#___ => False
#x => True
#get_value => True
#get value => False
#get!value => False
#some_super_puper_value => True
#Get_value => False
#get_Value => False
#getValue => False
#3m => False
#m3 => True
#assert => False
#assert_exception => True
import string
import keyword

name = input()
if not name :
    print(False)
elif name[0].isdigit():
    print(False)
elif any(char.isupper() for char in name):
    print(False)
elif name.count("_") > 1:
    print(False)
elif any(char in string.punctuation.replace("_", "") for char in name):
    print(False)
elif " " in name:
    print(False)
elif name in keyword.kwlist:
    print(False)
else:
    print(True)
