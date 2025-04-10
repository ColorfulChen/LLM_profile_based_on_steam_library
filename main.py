from tools.api import get_owned_game_data_from_steam,llm_output
import json
import time

if __name__ == "__main__":
    steam_library_data = get_owned_game_data_from_steam()
    filter_data = [item for item in steam_library_data["response"]["games"] if item["playtime_forever"] > 300]
    intro = llm_output(json.dumps(filter_data, indent=4))
    out_file = "output-" + str(int(time.time())) + ".md"
    with open(out_file, "w+", encoding="utf-8") as f:
        f.write(intro)