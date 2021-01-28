from l_00_inventory import csv_inventory
import csv
from pprint import pprint

# CONVERT INVENTORY TO CSV AND WRITE TO FILE
with open("l_00_inventory.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(csv_inventory)

# READ CSV INVENTORY FROM FILE
with open("l_00_inventory.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    saved_csv_inventory = list()
    for device in csv_reader:
        saved_csv_inventory.append(device)

# PRINT CSV INVENTORY STRING
print("l_00_inventory.csv file:\n", saved_csv_inventory)

# PRETTY PRINT
print("\ncsv pretty version:")
pprint(saved_csv_inventory)

# COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
if saved_csv_inventory == csv_inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")

# TURN LIST OF LISTS INTO DICTIONARY
devices = list()
for device_info in range(1, len(csv_inventory)):
    device = dict()
    for index, header in enumerate(csv_inventory[0]):
        device[header] = csv_inventory[device_info][index]
    devices.append(device)

# PRETTY PRINT DEVICES AS LIST OF DICTS
print("\n----- Devices as list of dicts --------------------")
pprint(devices)
