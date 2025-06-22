import json, datetime
with open("output.json", "w") as f:
    json.dump({"scraped_at": datetime.datetime.now().isoformat()}, f)
