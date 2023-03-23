#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def delete(d,output_d):
  global budget,fuel_type,body_type,transmission
  a=input("Model Name(Enter a string): ")
  try1()
  filter_1=filter01(d,budget)
  filter_2=filter_1[body_type]
  filter_3=filter_2[transmission]
  filter_4=filter_3[fuel_type]
  filter_4.remove(a)
  del output_d[a]
  print("\nData has been deleted.\n")

