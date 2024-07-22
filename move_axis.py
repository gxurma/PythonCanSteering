import requests
import json

PRINTER = "http://10.0.111.50:8080/api/v1"
printer_axis_name = "TableSlots.TableSlots.TableSlotLeft.Axis"

printer_pos3_mm = 735.0
printer_pos2_mm = 300.0
printer_pos1_mm = 100.0
printer_pos0_mm = 0.0

printer_speed_mmps = 200.0

data = {
    "Axis": printer_axis_name,
    "Position": printer_pos2_mm,
    "Speed": printer_speed_mmps
}

print("Sending", json.dumps(data, indent=4, sort_keys=True))

res = requests.post(f"{PRINTER}/functions/moveAxis", json=data)
if res.status_code != 200:
    print(f"Statuscode: {res.status_code}")
else:
    print("Result", json.dumps(res.json(), indent=4, sort_keys=True))

done = False
while not done:
    res = requests.get(f"{PRINTER}/components/TableSlots/TableSlots/TableSlotLeft/Axis")
    data = res.json()
    busy = data["busy"]
    inpos = data["inPosition"]
    pos = data["position"]
    print(f"{pos} mm busy: {busy} inpos: {inpos}",end="\r")
    if not busy:
        print()
        break
