import requests

def get_game_info(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=de&l=german"
    response = requests.get(url)
    return response.json()

def get_game_price(appid):
    data = get_game_info(appid)
    result = data[str(appid)]["data"]["price_overview"]
    return result

result = get_game_price(1245620)
print(result)