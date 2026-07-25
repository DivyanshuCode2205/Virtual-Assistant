# Virtual Assistant

A Python-based virtual assistant project that listens for commands and performs desktop and web automation tasks such as opening apps, opening websites, controlling tabs, searching online, and playing music.

## Features

- Listen for user commands.
- Open desktop applications.
- Open websites in the browser.
- Perform online searches.
- Automate browser tabs.
- Play music using Spotify or YouTube.
- Check internet connectivity before running online features.
- Organize automation features in separate Python modules.

## Project Structure

```bash
Virtual-Assistant/
│
├── Virtual_Assistant.py
├── requirement.txt
├── .gitignore
│
└── Automation/
    ├── Automation_Brain.py
    ├── Online_Search.py
    ├── Open_App.py
    ├── Play_music_Spotify.py
    ├── Tab_Automation.py
    ├── Web_Open.py
    ├── music_control.py
    ├── music_play_yt.py
    ├── DATA/
    └── Special_files/
```

## How It Works

The main file starts the assistant, checks internet-related functionality, starts the listener, and sends detected commands to the main automation logic.

## Requirements

Install Python 3.10+ recommended, then install the required packages:

```bash
pip install -r requirements.txt
```

> Note: I would suggest to use a Virtual environment, to isolate the dependencies of this project from the Main environment.

## Run the Project

```bash
python Virtual_Assistant.py
```

## Main Modules

- `Virtual_Assistant.py` - entry point of the project.
- `Automation/Automation_Brain.py` - main command handling logic.
- `Automation/Open_App.py` - opens desktop applications.
- `Automation/Web_Open.py` - opens websites.
- `Automation/Online_Search.py` - performs online search tasks.
- `Automation/Tab_Automation.py` - handles browser tab automation.
- `Automation/Play_music_Spotify.py` - plays music through Spotify.
- `Automation/music_play_yt.py` - plays music through YouTube.
- `Automation/music_control.py` - handles music control actions.
- `Automation/Special_files/` - helper utilities such as special support logic.

## Why This Project

This project is part of learning and building a more efficient personal virtual assistant that can handle real-world tasks better and more reliably.

## Author

**Divyanshu**

GitHub: [DivyanshuCode2205](https://github.com/DivyanshuCode2205)
