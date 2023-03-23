#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Takes input from the user about the details of the car and adds it to the existing data.


def add(d,output_d):
  global budget,fuel_type,body_type,transmission
  a=input("Model Name(Enter a string): ")
  b=input("Manufacturer(Enter a string): ")
  c=int(input("Base Price(Enter a number): "))
  try1()
  filter_1=filter01(d,budget)
  filter_2=filter_1[body_type]
  filter_3=filter_2[transmission]
  filter_4=filter_3[fuel_type]
  filter_4.append(a)
  output_d[a]=[b,str(c)]
  print("\n*****Data has been added*****\n")
  
  

