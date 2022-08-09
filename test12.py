#isidentifier

var="Sahal"
print(var.isidentifier())

var="Sahal12"
print(var.isidentifier())

var="12Sahal"
print(var.isidentifier())

var="Sahal12@"
print(var.isidentifier())

var="_Sahal"
print(var.isidentifier())

var="12"
print(var.isidentifier())

var="Sahal!"
print(var.isidentifier())

#isspace

var="Sahal   Sahal"
print(var.isspace())

var="    "
print(var.isspace())

#istitle

var="Luminar Technolab"
print(var.istitle())

var="Luminar technolab"
print(var.istitle())

#isupper

var="Luminar Technolab"
print(var.isupper())

var="LOST"
print(var.isupper())

#islower

var="Luminar Technolab"
print(var.islower())

var="lost"
print(var.islower())
