# TobyBot
## Pre-reqs:
* Discord bot created and added to a server
* Discord bot token

## Setup
* Install python

Python commands are in context of Windows. Use `py` in Windows instead of `python` for Unix.
* Create python virtual environment `py -m venv .venv`.
* Activate the venv as the Python Interpreter
* Install requirements `pip install -r requirements.txt`
* Create launch.json file in the .vscode folder. Paste and save the following. 
  * Environment variables:
    * TOKEN = your Discord bot token
    * ADMIN = your Discord name (not-alias) - enforces admin-only commands
    * CURRENCY = your desired currency name for the server
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
            "ADMIN": "<admin name>", 
            "CURRENCY": "<type of currency>"
        }
      }
    ]
  }
  ```
  * Debug the solution

## Currently Supported Commands:
`!hello`
  Bot says hello.

`!rumble`
  *admin-only function*
  Distributes royal-rumble numbers to everyone in the voice channel.

`!win_rumble [winner_name]`
  *admin-only function*
  Provides the winner of the royal-rumble the winnings.

`!start_bank`
  *admin-only function*
  Initializes funds for everyone in the voice channel.  People who previously had funds will be unaffected.

`!bank`
  Outputs the current funds for everyone in the bank.

`!my_funds`
  Outputs the requester's current funds in the bank.

`!grant_funds [target_name] [new_funds]`
  *admin-only function*
  Grants the designated user the funds allocated.
