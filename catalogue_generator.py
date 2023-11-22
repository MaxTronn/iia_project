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

# ITEM LIST FORMAT :
# - "categories"
# - "sub_categories" (optional)
# - "brand"
# - "type" / "name"

df = pd.DataFrame(columns=['id', 'description',
                  'image', 'service_list', 'item_list'])

df = df.append({'id': 1,
                'description': "living room",
                'image': 'https://images.unsplash.com/photo-1585412727339-54e4bae3bbf9?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'service_list': ["electrician", "carpenter", "painter"],
                'item_list': [["Tables", "IKEA", "metal"], ["Sofas", "LuxuryLoungers", "leather"],
                              ["Chairs", "CozyHome", "Ergonomic Chair"], [
                                  "electrical_supplies", "wires", "Acme Wires", "copper wire"],
                              ["building_materials", "paint",
                                  "Acme Paints", "Crimson Red"],
                              ["safety_equipment", "gloves", "SureGrip",
                                  "Protective Gloves"], ["TVs", "Vizio", "OLED"],
                              ["Home Appliances", "Sony", "air conditioner"]]}, ignore_index=True)

df = df.append({'id': 2,
                'description': "kitchen",
                'image': 'https://images.unsplash.com/photo-1588854337236-6889d631faa8?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'service_list': ["electrician", "carpenter", "painter", "mason", "plumber"],
                'item_list': [["Tables", "IKEA", "metal"], ["Chairs", "CozyHome", "Ergonomic Chair"],
                              ["electrical_supplies", "wires",
                                  "Acme Wires", "copper wire"],
                              ["tools", "power_tools", "Bosch", "Electric Drill"],
                              ["building_materials", "paint",
                                  "Acme Paints", "Crimson Red"],
                              ["safety_equipment", "gloves",
                                  "SureGrip", "Protective Gloves"],
                              ["Home Appliances", "Sony", "air conditioner"],
                              ["Cabinets", "CabinetDesigns", "Teak Cabinet"]]}, ignore_index=True)

df = df.append({'id': 3,
                'description': "bedroom",
                'image': 'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'service_list': ["electrician", "carpenter", "painter", "mason"],
                'item_list': [["electrical_supplies", "wires", "Acme Wires", "copper wire"],
                              ["tools", "power_tools", "Bosch", "Electric Drill"],
                              ["Beds", "Casper", "King Size Bed"], [
                                  "Chairs", "CozyHome", "Ergonomic Chair"],
                              ["building_materials", "paint",
                                  "Acme Paints", "Crimson Red"],
                              ["safety_equipment", "gloves",
                                  "SureGrip", "Protective Gloves"],
                              ["Home Appliances", "Sony", "air conditioner"],
                              ["Cabinets", "CabinetDesigns", "Teak Cabinet"]]}, ignore_index=True)

df = df.append({'id': 4,
                'description': "bathroom",
                'image': 'https://images.unsplash.com/photo-1572742482459-e04d6cfdd6f3?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'service_list': ["electrician", "carpenter", "painter", "mason", "plumber"],
                'item_list': [["electrical_supplies", "wires", "Acme Wires", "copper wire"],
                              ["tools", "power_tools", "Bosch", "Electric Drill"],
                              ["building_materials", "paint",
                                  "Acme Paints", "Crimson Red"],
                              ["safety_equipment", "gloves",
                                  "SureGrip", "Protective Gloves"],
                              ["TVs", "Vizio", "OLED"], [
                                  "Home Appliances", "Sony", "air conditioner"],
                              ["Cabinets", "CabinetDesigns", "Teak Cabinet"]]}, ignore_index=True)

df = df.append({'id': 5,
                'description': "office",
                'image': 'https://images.unsplash.com/photo-1600494603989-9650cf6ddd3d?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'service_list': ["electrician", "carpenter", "painter", "mason"],
                'item_list': [["electrical_supplies", "wires", "Acme Wires", "copper wire"],
                              ["tools", "power_tools", "Bosch", "Electric Drill"],
                              ["building_materials", "paint",
                                  "Acme Paints", "Crimson Red"],
                              ["safety_equipment", "gloves",
                                  "SureGrip", "Protective Gloves"],
                              ["TVs", "Vizio", "OLED"], [
                                  "Home Appliances", "Sony", "air conditioner"],
                              ["Cabinets", "CabinetDesigns", "Teak Cabinet"],
                              ["Tables", "IKEA", "metal"], [
                                  "Chairs", "CozyHome", "Ergonomic Chair"],
                              ["Laptops", "Dell", "Dell XPS 13"],
                              ["Smartphones", "Apple", "iPhone 12"]]}, ignore_index=True)

df.to_json('data/catalogue.json', orient='records')
