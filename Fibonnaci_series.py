frequency =13
fib_number1=0
fib_number2=1
for i in range(frequency):
    if i == 0:
        print(fib_number1,end=",")
    elif i == 1:
        print(fib_number1,end=",")
    else:
        fib_number = fib_number1+fib_number2
        print(fib_number,end=",")
        fib_number1=fib_number2
        fib_number2=fib_number
        
print("......")        
  
