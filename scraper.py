import pandas as pd
import json

with open("input.html") as f:
    htmlContent = f.read()
    data = pd.read_html(htmlContent)[0]


with open("sample.json") as f:
    output = json.load(f)

for i in range(len(data)):
    slot = {
        "id": output['details'][0]['name']+str(i),
        "theoryslot": data["Slot Detail"][i],
        "venue" : data["Venue"][i],
        "faculty": data["Faculty"][i],
    }
    output["details"][0]["slots"].append(slot)

with open(f"{output['type']}/{output['details'][0]['name']}.json",'w') as f:
    f.write(json.dumps(output, indent = 4))


