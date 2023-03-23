#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
  xyz=int(input("What would you like to do(Enter a number):\n1. Search.\n2. Add Data.\n3. Delete Data.\n4. Exit.\n"))
  if xyz==1:
    filter(d,output_d)
  elif xyz==2:
    add(d,output_d)
  elif xyz==3:
    delete(d,output_d)
  elif xyz==4:
    break

