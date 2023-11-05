from flask import Flask, request, jsonify
import os
import json
import requests

app = Flask(__name__)

def read_json_file(directory, file_name):
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data  # Return the JSON object

@app.route('/catalogue/<id>')
def get_electrical_item(id):
    data = read_json_file("./data", "catalogue.json")
    id = int(id)
    item_list = []
    services_list = []
    for obj in data:
        if(obj["id"] == id):
            item_list = obj["item_list"]
            services_list = obj["service_list"]
            break

    electricalItems = []
    furnitureItems = []
    generalItems = []

    for item in item_list:
        if(item[0] == "Laptops" or item[0] == "TVs" or item[0] == "Home Appliances" or item[0] == "Smartphone"):
            print("*******ELECTRICAL******")
            if(item[0] == "TVs"):
                electricalItems.append({
                    "item_category": item[0],
                    "item_brand": item[1],
                    "item_type": item[2] 
                })
            else:
                electricalItems.append({
                    "item_category": "Home_Appliances" if item[0] == "Home Appliances" else item[0],
                    "item_brand": item[1],
                    "item_name": item[2] 
                })
        elif(item[0] == "Tables" or item[0] == "Cabinets" or item[0] == "Beds" or item[0] == "Sofas" or item[0] == "Chairs"):
            print("*******FURNITURE******")
            furnitureItems.append({
                "item_category": item[0],
                "item_brand": item[1],
                "item_type": item[2]
            })
        elif(item[0] == "building_materials" or item[0] == "safety_equipments" or item[0] == "electrical_supplies" or item[0] == "tools"):
            print("*******General Hardware******")
            generalItems.append({
                "item_category": item[0],
                "item_subcategory": item[1],
                "item_brand": item[2],
                "item_name": item[3]
            })

    electricalURL = "http://127.0.0.1:5001/items/electrical"
    electricalData = []
    print(electricalItems)
    for itemDict in electricalItems:
        response = requests.get(electricalURL, itemDict)
        if(response.status_code == 200):
            electricalData.append(response.json())

    furnitureURL = "http://127.0.0.1:5001/items/furniture"
    furnitureData = []
    for itemDict in furnitureItems:
        response = requests.get(furnitureURL, itemDict)
        if(response.status_code == 200):
            furnitureData.append(response.json())

    generalHardwareURL = "http://127.0.0.1:5001/items/general-hardware"
    generalHardwareData = []
    for itemDict in generalItems:
        response = requests.get(generalHardwareURL, itemDict)
        if(response.status_code == 200):
            generalHardwareData.append(response.json())

    services = []

    for service in services_list:
        serviceURL = "http://127.0.0.1:5002/get-services/"
        serviceURL = serviceURL + service
        response = requests.get(serviceURL)
        if(response.status_code == 200):
            services.append(response.json())

    responseObject = {
            "electrical": electricalData,
            "furniture": furnitureData,
            "generalHardware": generalHardwareData,
            "services": services
        }

    return responseObject


if __name__ == '__main__':
    app.run()
