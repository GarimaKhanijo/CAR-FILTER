def fuel5(n):
  if n==1:
    return "electric"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Electric
**************************
'''))
    return fuel5(x)

def fuel6(n):
  if n==1:
    return "diesel"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Diesel
**************************
'''))
    return fuel6(x)

def fuel7(n):
  if n==1:
    return "petrol"
  elif n==2:
    return "cng"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Petrol
  2. CNG
**************************
'''))
    return fuel7(x)

def fuel8(n):
  if n==1:
    return "diesel"
  elif n==2:
    return "electric"
  elif n==3:
    return "petrol"
  elif n==4:
    return "cng"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Diesel
  2. Electric
  3. Petrol
  4. CNG
**************************
'''))
    return fuel8(x)

