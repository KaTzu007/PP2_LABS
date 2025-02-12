from tabulate import tabulate
import json

with open(r".\JSON\sample-data.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)

list = []


for i in range(0, 3):
    sublist = []
    sublist.append(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"])
    sublist.append(data["imdata"][i]["l1PhysIf"]["attributes"]["descr"])
    sublist.append(data["imdata"][i]["l1PhysIf"]["attributes"]["speed"])
    sublist.append(data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
    list.append(sublist)

headers = ["DN", "Description", "Speed", "MTU"]

print(tabulate(list, headers=headers))
