#split string into list format

split_string1="hello world"
split_string2="hello/world"
split_string3="hello*world*sahal"
split_string4="hello.world"

print(split_string1.split(" "))
print(split_string2.split("/"))
print(split_string3.split("*"))
print(split_string4.split("."))

#padding
center_string="Helo World"
print(center_string.center(20,"-"))

#count
count_string="Sahal Sahal Sahal Godwin"
print(count_string.count("Sahal"))

#check the end of the string and return true/false
endswith_string="Hello World"
print(endswith_string.endswith("d"))











