def calculator(num1,num2,op):
  if op=="Addition":
    return num1+num2
  elif op=="Multiplication":
    return num1*num2
  elif op=="Subraction":
    return num1-num2
  elif op=="Division":
    return num1/num2
  elif op=="Modulous":
    return num1%num2
  elif op=="Floor Division":
    return num1//num2
  elif op=="Exponentiation":
    return num1**num2
  else:
    return False
num1=int(input("Enter A Number:"))
num2=int(input("Enter A Number:"))
op=input("Enter an operation choose from Addition,Subraction,Multiplication,Division,Modulous,Floor Division,Exponentiation:")
print(calculator(num1,num2,op))
