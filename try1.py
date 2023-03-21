#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def try1():
  budget,fuel_type,body_type,transmission
  budget=int(input('''
  Enter Budget:
  1. Below 10 lakhs
  2. 10-20 lakh
  3. 20-30 lakh
  4. 30-40 lakh
  5. 40-50 lakh
'''))

  if budget==1:
    a=int(input('''
  Enter Body Type:
  1. Compact Sedan
  2. Compact SUV
  3. Hatchback
  4. MUV
  5. Sedan
  6. SUV
'''))
    body_type=body1(a)

  if budget==2:
    a=int(input('''
  Enter Body Type:
  1. Compact SUV
  2. Hatchback
  3. MUV
  4. Sedan
  5. SUV
'''))
    body_type=body2(a)
  
  if budget==3:
    a=int(input('''
  Enter Body Type:
  1. SUV
'''))
    body_type=body3(a)

  if budget==4:
    a=int(input('''
  Enter Body Type:
  1. Hatchback
  2. SUV
'''))
    body_type=body4(a)

  if budget==5:
    a=int(input('''
  Enter Body Type:
  1. Hatchback
  2. Sedan
  3. SUV
'''))
    body_type=body5(a)


  if ((budget==2 or budget==4) and (body_type=="hatchback")) or budget==5:
    b=int(input('''
  Enter Transmission:
  1. Automatic
'''))
    transmission=transm1(b)

  else:
    b=int(input('''
  Enter Transmission:
  1. Manual
  2. Automatic
'''))
    transmission=transm2(b)


  if (budget==2 and body_type=="muv") or (budget==1 and body_type=="compact sedan") or (budget==1 and body_type=="hatchback" and transmission=="manual"):
    c=int(input('''
  Enter Fuel Type:
  1. Diesel
  2. Petrol
  3. CNG
'''))
    fuel_type=fuel1(c)  

  if ((budget==1 or budget==2) and body_type=="sedan") or (budget==1 and body_type=="compact suv") or (budget==4 and body_type=="suv"):
    c=int(input('''
  Enter Fuel Type:
  1. Diesel
  2. Petrol
'''))
    fuel_type=fuel2(c)  

  if (budget==5 and (body_type=="suv" or body_type=="sedan")) or (budget==2 and body_type=="suv"):
    c=int(input('''
  Enter Fuel Type(Enter a number):
  1. Diesel
  2. Electric
  3. Petrol
'''))
    fuel_type=fuel3(c) 

  if (budget==1 and body_type=="suv") or (budget==2 and body_type=="compact suv") or (budget==5 and body_type=="hatchback"):
    c=int(input('''
  Enter Fuel Type:
  1. Petrol
'''))
    fuel_type=fuel4(c) 

  if (budget==2 or budget==4) and body_type=="hatchback":
    c=int(input('''
  Enter Fuel Type:
  1. Electric
'''))
    fuel_type=fuel5(c) 

  if budget==3:
    c=int(input('''
  Enter Fuel Type:
  1. Diesel
'''))
    fuel_type=fuel6(c)

  if budget==1 and body_type=="muv":
    c=int(input('''
  Enter Fuel Type:
  1. Petrol
  2. CNG
'''))
    fuel_type=fuel7(c)
  if (budget==1 and body_type=="hatchback") and transmission=="automatic":
    c=int(input('''
  Enter Fuel Type:
  1. Diesel
  2. Electric
  3. Petrol
  4. CNG

'''))
    fuel_type=fuel8(c)

