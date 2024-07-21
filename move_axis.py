import requests
import json

HOST = "http://127.0.0.1:8080/api/v1"
axis_name = "TableSlots.TableSlots.TableSlotLeft.Axis"
pos_mm = 300.0
speed_mmps = 200.0

data = {
    "Axis": axis_name,
    "Position": pos_mm,
    "Speed": speed_mmps,
}

print("Sending", json.dumps(data, indent=4, sort_keys=True))

res = requests.post(f"{HOST}/functions/moveAxis", json=data)
if res.status_code != 200:
    print(f"Statuscode: {res.status_code}")
else:
    print("Result", json.dumps(res.json(), indent=4, sort_keys=True))

done = False
while not done:
    res = requests.get(f"{HOST}/components/TableSlots/TableSlots/TableSlotLeft/Axis")
    data = res.json()
    busy = data["busy"]
    inpos = data["inPosition"]
    pos = data["position"]
    print(f"{pos} mm busy: {busy} inpos: {inpos}")
    if not busy:
        break
