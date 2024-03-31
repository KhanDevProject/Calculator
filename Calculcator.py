def add(x, y):  
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   return x * y 
def divide(x, y): 
   return x / y  

# take input from the user  
def main():
  print("Select operation.")  
  print("1.Add")  
  print("2.Subtract")  
  print("3.Multiply")  
  print("4.Divide")  
main()

def main1():
  print("\nIf you want to go back to homepage")
  print("You can hit enter to continue")
  a = input("enter (q): ")
  if a == "q":
    main2()
    
choice = input("Enter choice(1,2,3,4): ")  
def main2():
  while True: 
    num1 = int(input("Enter first number: "))  
    num2 = int(input("Enter second number: "))
    if choice == '1':  
      print(f"{num1} + {num2} = {add(num1,num2)}")
      main1()
    elif choice == '2':
      print(f"{num1} - {num2} = {subtract(num1,num2)}")
      main1()  
    elif choice == '3':
      print(f"{num1} * {num2} = {multiply(num1,num2)}")  
      main1()
    elif choice == '4':  
      print(f"{num1} / {num2} = {divide(num1,num2)}")
      main1()  
    elif "".__eq__(choice):
      break
    else:  
      print("Invalid input")  
main2()
