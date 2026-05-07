num = int(input("enter a number: "))
temp = num 
sum = 0
while temp != 0:
        rem = temp%10
        sum = sum + rem
        temp = temp//10 
        if sum >9 and num == 0:
            num = sum
            sum = 0 

print('your lucky digit is : ', sum)

