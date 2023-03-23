#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def transm1(n):
  if n==1:
    return "automatic"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Transmission(Enter a number):
  1. Automatic
**************************
'''))
    return transm1(x)

def transm2(n):
  if n==1:
    return "manual"
  elif n==2:
    return "automatic"
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Transmission(Enter a number):
  1. Manual
  2. Automatic
**************************
'''))
    return transm2(x)

