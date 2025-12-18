def sum(a, b):
  return a + b
def substraction(a, b):
  return a - b
def multiplication(a, b):
  return a * b
def division(a, b):
  if b != 0:
     return a / b
  else:
     print("Erreur : division par zéro")
x= float(input("Entrez le premier nombre : "))
y= float(input("Entrez le deuxième nombre : "))
print(f"{x} + {y} = {sum(x,y)}")
print(f"{x} - {y} = {substraction(x,y)}")
print(f"{x} * {y} = {multiplication(x,y)}")
print(f"{x} / {y} = {division(x,y)}")

