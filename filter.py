def filter(d,output_d):
  global budget,fuel_type,body_type,transmission
  try1()
  filter_1=filter01(d,budget)
  filter_2=filter_1[body_type]
  filter_3=filter_2[transmission]
  filter_4=filter_3[fuel_type]
  print("\nRecommended cars are:\n")
  for i in filter_4:
    print()
    print("**************************")
    print("Model Name: "+i.upper())
    print("Manufacturer: "+output_d[i][0].upper())
    print("Base Price: "+output_d[i][1])
    print("Fuel Type: "+fuel_type.upper())
    print("Transmission: "+transmission.upper())
    print("Body Type: "+body_type.upper())
    print("**************************")
    print()
