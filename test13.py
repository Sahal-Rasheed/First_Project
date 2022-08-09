#join

join_list=['a','b','c']
print('#'.join(join_list))

#partition

string_partition="luminartechnolab"
print(string_partition.partition('t'))

a="sahal&godwin"
print(a.partition('&'))

#replace
a="breaking lost"
print(a.replace("lost","bad"))

a="Joseph is a good,Joseph is a God,Joseph is from brthlm"
print(a.replace("Joseph","Mary",2))

#startswith

startswith_string="Say my name"
print(startswith_string.startswith("Say"))

#swapcase

a="Game of THRONES"
print(a.swapcase())