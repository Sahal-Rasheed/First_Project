#tuple->list->tuple

tuplee=(1,2,3,4)
tuplee=list(tuplee)
#print(tuplee)
tuplee.append(tuplee)
tuplee=tuple(tuplee)
print(tuplee)