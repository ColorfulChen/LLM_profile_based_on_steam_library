from tools.api import get_owned_game_data_from_steam,llm_output
import json
import time

if __name__ == "__main__":
    steam_library_data = get_owned_game_data_from_steam()

    print("filtering game data from steam...")
    filter_data = []
    for item in steam_library_data["response"]["games"]:
        if item["playtime_forever"] > 0:
            last_play_time = time.strftime("%Y-%m-%d", time.localtime(item["rtime_last_played"]))
            playtime = round(float(item["playtime_forever"]) / 60, 1)
            filter_data.append(
                {
                    "name": item["name"],
                    "playtime": playtime,
                    "last_play_time": last_play_time,
                }
            )
    print("filtering data success!")

    print("generating intro...")
    intro = llm_output(json.dumps(filter_data, indent=4))
    print("generating intro success!")

    print(intro)

    print("writing to file...")
    out_file = "output-" + str(int(time.time())) + ".md"
    with open(out_file, "w+", encoding="utf-8") as f:
        f.write(intro)
    print("writing to file success!")