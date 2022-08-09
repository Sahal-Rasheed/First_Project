Testing----------------------------------------------------------------------

num=12345 #declare a number to a variable
sum=0 #initialize sum as zero
for i in range(len(str(num))): #convert integer to string and take its length
    temp=num%10  #declare a variable temp & find reminder of num and assign it to temp
    num=num//10  #perform floor division to eliminate the last digit of num
    sum+=temp    #add the value in temp to the sum variable
print(sum)
