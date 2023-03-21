#!/usr/bin/env python
# coding: utf-8

# In[ ]:


d={
   1:{"hatchback":{"manual":{"petrol":["i20","Glanza","Baleno","Altroz","Swift","C3","Wagon R","Grand i10 Nios"],
                             "cng":["Glanza","Baleno","Swift","Wagon R","Grand i10 Nios"],
                             "diesel":["i20","Altroz","Grand i10 Nios"]},
                   "automatic":{"electric":["Tiago EV"],
                             "petrol":["i20","Glanza","Baleno","Altroz","Swift","Wagon R","Grand i10 Nios"],
                             "cng":["Glanza","Baleno","Swift","Wagon R","Grand i10 Nios"],
                             "diesel":["i20","Altroz","Grand i10 Nios"]
                                }},
      "compact suv":{"manual":{"petrol":["KUV 100 NXT","WR-V","Urban Cruiser","Kiger","Punch","Sonet","Venue","Nexon","Breeza","XUV 300"],
                               "diesel":["Bolero","Bolero Neo","WR-V","XUV 300","Nexon","Venue","Sonet"]},
                     "automatic":{"petrol":["Urban Cruiser","Kiger","Punch","Sonet","Venue","Nexon","Breeza","XUV 300"],
                               "diesel":["XUV 300","Nexon","Venue","Sonet"]}},
      "muv":{"manual":{"petrol":["Ertiga","Triber"],"cng":["Ertiga"]},
             "automatic":{"petrol":["Ertiga","Triber"],"cng":["Ertiga"]}},
      "compact sedan":{"manual":{"petrol":["Dzire","Aura"],"cng":["Dzire","Aura"],"diesel":["Aura"]},
                        "automatic":{"petrol":["Dzire","Aura"],"cng":["Dzire","Aura"],"diesel":["Aura"]}},
      "suv":{"manual":{"petrol":["S Cross"]},
                     "automatic":{"petrol":["S Cross"]}},
      "sedan":{"manual":{"petrol":["Ciaz","Verna"],"diesel":["Verna"]},
                     "automatic":{"petrol":["Ciaz","Verna"],"diesel":["Verna"]}}},
   2:{"muv":{"manual":{"petrol":["Carens","Innova Crysta"],"cng":["XL6"],"diesel":["Carens","Innova Crysta"]},
             "automatic":{"petrol":["Carens","Innova Crysta"],"cng":["XL6"],"diesel":["Carens","Innova Crysta"]}},
      "suv":{"manual":{"petrol":["Thar","Astor","Creta","Grand Vitara","Urban Cruiser Hyryder","Kushaq","Scorpio-N","XUV 700","Hector","Compass"],
                       "diesel":["Thar","Creta","Scorpio-N","Scorpio Classic","XUV 700","Hector","Harrier","Safari","Compass"],
                       "electric":["Grand Vitara","Urban Cruiser Hyryder"]},
             "automatic":{"petrol":["Thar","Astor","Creta","Grand Vitara","Urban Cruiser Hyryder","Kushaq","Scorpio-N","XUV 700","Hector","Compass"],
                          "diesel":["Thar","Creta","Scorpio-N","XUV 700","Hector","Harrier","Safari","Compass"],
                          "electric":["Grand Vitara","Urban Cruiser Hyryder"]}},

      "compact suv":{"manual":{"petrol":["XUV300 TurboSport"]},
                     "automatic":{"petrol":["Venue N Line"]}},
      "sedan":{"manual":{"petrol":["Slavia","Virtus","New City"],"diesel":["New City"]},
                     "automatic":{"petrol":["Slavia","Virtus","New City"],"diesel":["New City"]}},
      "hatchback":{"automatic":{"electric":["Tigor EV"]}}},
   3:{"suv":{"manual":{"diesel":["Meridian"]},
             "automatic":{"diesel":["Meridian"]}}},
   4:{"suv":{"manual":{"diesel":["Fortuner"],"petrol":["Fortuner"]},
             "automatic":{"diesel":["Alturas G4","Fortuner","MU-X","C5 Aircross"],"petrol":["Fortuner","Q2"]}},
      "hatchback":{"automatic":{"electric":["Atto 3"]}}},
   5:{"hatchback":{"automatic":{"petrol":["Cooper","Countryman","Cooper JCW"]}},
      "suv":{"automatic":{"diesel":["X1"],"electric":["XC40"],"petrol":["X1","Q3","XC40"]}},
      "sedan":{"automatic":{"petrol":["A-Class Limousine","A4","GLA","Camry","S60","3 Series"],"diesel":["A-Class Limousine","GLA","3 Series"],
                            "electric":["Camry","S60"]}}}   
}

output_d={
    "Aura":["Hyundai","6,09,000"],"Dzire":["Maruti Suzuki","6,23,000"],"Kiger":["Renault","5,99,000"],"Punch":["Tata","6,00,000"],
    "KUV 100 NXT":["Mahindra","6,21,000"],"Sonet":["Kia","7,49,000"],"Venue":["Hyundai","7,53,000"],"XUV 300":["Mahindra","8,41,000"],
    "Nexon":["Tata","7,69,000"],"Breeza":["Maruti Suzuki","7,99,000"],"Urban Cruiser":["Toyota","9,02,000"],"WR-V":["Honda","9,25,000"],
    "Bolero Neo":["Mahindra","9,48,000"],"Bolero":["Mahindra","9,53,000"],"XUV300 TurboSport":["Mahindra","10,35,000"],
    "Venue N Line":["Hyundai","12,16,000"],"Grand i10 Nios":["Hyundai","5,42,000"],"Wagon R":["Maruti Suzuki","5,47,000"],
    "C3":["Citroen","5,88,000"],"Swift":["Maruti Suzuki","5,91,000"],"Altroz":["Tata","6,00,000"],"Baleno":["Maruti Suzuki","6,42,000"],
    "Glanza":["Toyota","6,59,000"],"i20":["Hyundai","7,07,000"],"Tiago EV":["Tata","8,49,000"],"Tigor EV":["Tata","12,49,000"],
    "Atto 3":["BYD","30,00,000"],"Cooper":["Mini","40,00,000"],"Countryman":["Mini","46,00,000"],"Cooper JCW":["Mini","47,70,000"],
    "Triber":["Renault","5,90,000"],"Ertiga":["Maruti Suzuki","8,35,000"],"Carens":["Kia","10,00,000"],"XL6":["Maruti Suzuki","11,29,000"],
    "Innova Crysta":["Toyota","17,18,000"],"Ciaz":["Maruti Suzuki","8,78,000"],"Verna":["Hyundai","9,43,000"],"Slavia":["Skoda","11,29,000"],
    "Virtus":["Volkswagen","11,32,000"],"New City":["Honda","11,60,000"],"A-Class Limousine":["Mercedes-Benz","41,99,000"],"A4":["Audi","43,06,000"],
    "GLA":["Mercedes-Benz","44,90,000"],"Camry":["Toyota","45,25,000"],"S60":["Volvo","45,90,000"],"3 Series":["BMW","46,86,000"],
    "S Cross":["Maruti Suzuki","8,72,000"],"Thar":["Mahindra","10,02,000"],"Astor":["MG","10,32,000"],"Creta":["Hyundai","10,44,000"],
    "Grand Vitara":["Maruti Suzuki","10,45,000"],"Urban Cruiser Hyryder":["Toyota","10,48,000"],"Kushaq":["Skoda","11,58,000"],
    "Scorpio-N":["Mahindra","11,99,000"],"Scorpio Classic":["Mahindra","11,99,000"],"XUV 700":["Mahindra","13,45,000"],"Hector":["MG","14,42,000"],
    "Harrier":["Tata","14,79,000"],"Safari":["Tata","15,45,000"],"Compass":["Jeep","19,27,000"],"Meridian":["Jeep","29,90,000"],
    "Alturas G4":["Mahindra","30,68,000"],"Fortuner":["Toyota","32,58,000"],"MU-X":["Isuzu","34,94,000"],"Q2":["Audi","35,00,000"],
    "C5 Aircross":["Citroen","36,67,000"],"X1":["BMW","41,45,000"],"Q3":["Audi","44,89,000"],"XC40":["Volvo","45,85,000"]
}

