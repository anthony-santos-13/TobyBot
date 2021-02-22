# TobyBot
## Pre-reqs:
* Discord bot created and added to a server
* Discord bot token

## Setup
* Install python

Python commands are in context of Windows. Use `python` instead of `py` for Unix.
* Create python virtual environment `py -m venv .venv`.
* Activate the venv as the Python Interpreter
* Install requirements `pip install -r requirements.txt`
* Create launch.json file in the .vscode folder. Paste and save the following
  * Replace `<token>` with your Discord bot token:
  * Replace `<bot_channels>` with single line string of channel ids, separated by spaces. These are for restricted commands.
```json
{
    "version": "0.2.0",
    "configurations": [
      {
        "type": "python",
        "request": "launch",
        "name": "Launch main",
        "program": "${workspaceFolder}\\packages\\TobyBot\\main.py",
        "env": {
            "TOKEN": "<token>",
            "BOT_CHANNELS": "<bot_channels>",
        }
      }
    ]
  }
  ```
  * Debug the solution

## Supported Commands
* `!hello` - Say hello to TobyBot!
* `!tobyclip` - Request a cool TobyStamkos gamerclip 😎.
* `!rumble` - Restricted command that only works during a Royal Rumble event. Randomly generates a 30-entrant Royal Rumble pool using the current members of the sender's voice channel.
* `!poll` - Restricted command. Generates a poll of up to 10 options. Requires the following syntax of command and brackets: !poll {Title} [Option1] [Option2] ... [OptionN]
* `!what` - WHAT?

Restricted commands can only be used in channels specified in the launch.json. The rest can be used anywhere.

## Please Note
Some of the solution currently contains hard-coded references to custom emoji on a private Discord server