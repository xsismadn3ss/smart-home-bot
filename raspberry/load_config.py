import json

async def load_config():
    with open("raspi_config.json", "r") as f:
        data = json.load(f)
    return data