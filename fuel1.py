def fuel1(n):
  if n==1:
    return "diesel"
  elif n==2:
    return "petrol"
  elif n==3:
    return "cng"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Diesel
  2. Petrol
  3. CNG
**************************
'''))
    return fuel1(x)

def fuel2(n):
  if n==1:
    return "diesel"
  elif n==2:
    return "petrol"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Diesel
  2. Petrol
**************************
'''))
    return fuel2(x)

def fuel3(n):
  if n==1:
    return "diesel"
  elif n==2:
    return "electric"
  elif n==3:
    return "petrol"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Diesel
  2. Electric
  3. Petrol
**************************
'''))
    return fuel3(x)

def fuel4(n):
  if n==1:
    return "petrol"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Fuel Type(Enter a number):
  1. Petrol
**************************
'''))
    return fuel4(x)
