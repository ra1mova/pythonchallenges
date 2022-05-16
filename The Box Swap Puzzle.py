#Swapping the content of two variables - www.101computing.net/the-box-swap-puzzle/

number1 = int(input("Enter a number between 1 and 10:"))
number2 = int(input("Enter a number between 1 and 10:"))
temp = 0 
if number1 > number2:
  pass 
if number1 < number2:
  temp = number1
  number1 = number2
  number2 = temp 
else:
  pass 
print(number1,number2)
#complete the code here...