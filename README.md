# LLM Profile Based on Steam Library

This project generates a personalized Steam profile introduction based on a user's Steam game library. It uses the Steam Web API to fetch game data and an LLM (Language Model) API to create a friendly, engaging, and creative profile introduction.

## Features

- **Steam Library Integration**: Fetches the user's Steam game library, including playtime and game details.
- **Data Filtering**: Filters games based on playtime to focus on the user's most-played games.
- **LLM-Powered Profile Generation**: Uses an LLM to analyze the user's game library and generate a personalized Steam profile introduction.
- **Customizable Output**: Outputs the generated profile to a text file for easy sharing or editing.

## Project Structure

```
LLM_profile_based_on_steam_library/
│
├── main.py                # Main script to run the project
├── tools/
│   ├── api.py             # Contains API integrations and helper functions
├── .env                   # Environment variables (API keys, user IDs, etc.)
└── output.md              # Generated Steam profile introduction
```

## Requirements

- Python 3.8+
- Steam Web API Key
- OpenAI-compatible API Key (e.g., DeepSeek)
- `requests` library
- `python-dotenv` library

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/LLM_profile_based_on_steam_library.git
   cd LLM_profile_based_on_steam_library
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add the following environment variables:
   ```
   STEAM_API_KEY=your_steam_api_key
   STEAM_USER_ID=your_steam_user_id
   DEEPSEEK_API_KEY=your_deepseek_api_key
   ```

4. Run the main script:
   ```bash
   python main.py
   ```

## How It Works

1. **Fetch Steam Library Data**: The `get_owned_game_data_from_steam` function in `api.py` retrieves the user's Steam library using the Steam Web API.
2. **Filter Data**: The script filters games with more than 10 hours of playtime (`playtime_forever > 600`).
3. **Generate Profile**: The `llm_output` function sends the filtered data to an LLM API, which generates a personalized Steam profile introduction.
4. **Save Output**: The generated profile is saved to `output.txt`.

## Example Output

The generated profile might look like this:

```
**🚀 Welcome to My Steam Profile! 🎮**  

Hey there, fellow gamer! 👋 I’m a huge fan of *deep dives* into immersive worlds and *chaotic fun* with friends. My library’s a wild mix of survival, shooters, RPGs, and quirky indies—because why stick to one genre when you can have it all?  

**🔥 Most-Played Obsessions:**  
- **Dead by Daylight ** – Guess I really love being chased by killers (or doing the chasing… no judgment). 😈  
- **Counter-Strike 2 ** – Still trying to convince myself I’m *not* addicted to tactical panic. 🔫  
- **Terraria ** – If building pixelated castles and fighting moon lords was a job, I’d be CEO. 🌙  
- **Tabletop Simulator ** – Because who needs physical board games when you can flip the virtual table? ♟️  

**🎮 Genre Hopper Extraordinaire:**  
I’ve got a soft spot for **survival games** (*The Forest, Project Zomboid*), **RPGs** (*Fallout, Witcher 3*), and **anything with co-op chaos** (*Lethal Company, Deep Rock Galactic*). Also, apparently **mahjong** (*MahjongSoul*)—because even warriors need a zen break. 🀄  

**💎 Hidden Gems in My Backpack:**  
- *The Stanley Parable* – Narrator still haunts my dreams.  
- *Crypt of the NecroDancer* – Dancing through dungeons like a rhythm-game wizard.  
- *eden** – Because sometimes you just need a *painfully beautiful* visual novel.  

**🤪 Quirky Confession:**  
I’ve spent *more time in Garry’s Mod* than some relationships last. Sandbox madness is my therapy. Also, *Mountain*—yes, the *literal* mountain simulator. I’m either a genius or need help. 🌄  

**🌟 Gaming Goals & Memories:**  
- **Current Mission:** Surviving *Helldivers 2* without team-killing my squad (oops).  
- **Proudest Moment:** Finally beating *Cuphead* after 15 hrs of rage (and tears).  
- **Dream Game:** A *Borderlands* x *Stardew Valley* mashup. Gearbox, *call me*.  

**👾 Let’s Play Sometime!**  
Whether it’s *looting in Darktide*, *screaming in Lethal Company*, or *failing puzzles in We Were Here*, I’m always down for shenanigans. Hit me up—just don’t blame me if things go *horribly wrong*. 😉  

*"Games don’t make us violent. Lag does."* – Me, probably. 🎮💥
```

## Notes

- Ensure your Steam profile is public for the API to fetch your game data.
- The LLM API requires an active API key and sufficient credits for usage.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API)
- [DeepSeek API](https://api.deepseek.com)
- OpenAI for inspiration in LLM-based applications
