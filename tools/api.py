import requests
import time
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

RETRY_DELAY = 5
MAX_RETRIES = 5
include_played_free_games='true'
STEAM_API_KEY = os.environ.get("STEAM_API_KEY")
STEAM_USER_ID = os.environ.get("STEAM_USER_ID")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")

def send_request_with_retry(
    url, headers=None, json_data=None, retries=MAX_RETRIES, method="patch"
):
    while retries > 0:
        try:
            if method == "patch":
                response = requests.patch(url, headers=headers, json=json_data)
            elif method == "post":
                response = requests.post(url, headers=headers, json=json_data)
            elif method == "get":
                response = requests.get(url)

            response.raise_for_status()  # 如果响应状态码不是200系列，则抛出HTTPError异常
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request Exception occurred: <{e}> Retring....")
            retries -= 1
            if retries > 0:
                time.sleep(RETRY_DELAY)  # 等待一段时间后再重试
            else:
                print("Max retries exceeded. Giving up.")
                return {}

def get_owned_game_data_from_steam():
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?"
    url = url + "key=" + STEAM_API_KEY
    url = url + "&steamid=" + STEAM_USER_ID
    url = url + "&include_appinfo=True"
    if include_played_free_games == "true":
        url = url + "&include_played_free_games=True"

    print("fetching data from steam..")

    try:
        response = send_request_with_retry(url, method="get")
        print("fetching data success!")
        return response.json()
    except Exception as e:
        print(f"Failed to send request: {e}")

def llm_output(steam_library_data):
   
    templete = """
I want you to act as a creative writer and generate a personalized Steam profile introduction based on the user's game library. 
The introduction should highlight the user's gaming preferences, favorite genres, and notable achievements. 
Use a friendly and engaging tone, and make it appealing to other gamers.

Here is the user's Steam library data:
{steam_library_data}

Analyze the data and include the following in the introduction:
1. Mention the user's most-played games and why they might enjoy them.
2. Highlight the user's favorite genres based on their library.
3. Include any unique or rare games in their collection.
4. Add a fun or quirky statement about their gaming habits if possible.
5. Add a personal touch, like a favorite gaming memory or a goal they have in gaming.
6. Use a friendly and engaging tone to make it appealing to other gamers.
7. make it a person, not a bot.
8. use more emojis.
9. make more personal feelings and less data.
10. make it more like a story, not just a list of games.
11. consider the user's last play time for each game, user's perference could change over time.

Make the introduction concise, creative, and no longer than 500 words.
"""
    prompt = templete.format(steam_library_data=steam_library_data)

    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    return response.choices[0].message.content