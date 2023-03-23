#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def filter01(di,n):
  if n in di:
    return di[n]
  else:
    print("OPPS!! We don't have that category.\nPlease choose again.")
    x=int(input('''**************************
  Enter Budget(Enter a number):
  1. Below 10 lakhs
  2. 10-20 lakh
  3. 20-30 lakh
  4. 30-40 lakh
  5. 40-50 lakh
**************************
'''))
    global budget
    budget=x
    return filter01(di,budget)

