import pandas as pd

'''
Electrical:
            "Laptops"
             "TVs"
            "Home Appliances"
             "Smartphones"
             
             
General Hardware :
            "building_materials",
          "safety_equipment",
          "electrical_supplies",
          "tools"
          
          
Furniture Shop:
          "Tables"
          "Cabinets"
          "Beds"
          "Sofas"
          "Chairs"
'''

df = pd.DataFrame(columns=['id','description', 'service_list', 'item_list'])

df = df.append({'id' : 1,
                'description': "living room",
                'service_list': ["electrician","carpenter","painter"],
                'item_list':["Tables","Sofas","Chairs","electrical_supplies",
                             "building_material","safety_equipment","TVs","Home Appliances"]}, ignore_index=True)

df = df.append({'id' : 2,
                'description': "kitchen",
                'service_list': ["electrician","carpenter","painter","mason","plumber"],
                'item_list':["Tables","Chairs","electrical_supplies","tools",
                             "building_material","safety_equipment","Home Appliances","Cabinets"]}, ignore_index=True)

df = df.append({'id' : 3,
                'description': "bedroom",
                'service_list': ["electrician","carpenter","painter","mason"],
                'item_list':["electrical_supplies","tools", "Beds", "Chairs"
                             "building_material","safety_equipment","Home Appliances","Cabinets"]}, ignore_index=True)

df = df.append({'id' : 4,
                'description': "bathroom",
                'service_list': ["electrician","carpenter","painter","mason","plumber"],
                'item_list':["electrical_supplies","tools", "building_material","safety_equipment", "TVs"
                             "Home Appliances","Cabinets"]}, ignore_index=True)

df = df.append({'id' : 5,
                'description': "office",
                'service_list': ["electrician","carpenter","painter","mason"],
                'item_list':["electrical_supplies","tools", "building_material","safety_equipment", "TVs"
                             "Home Appliances","Cabinets","Tables","Chairs","Laptops","Smartphones"]}, ignore_index=True)

df.to_json('data/catalogue.json', orient='records')