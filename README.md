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
* Create launch.json file in the .vscode folder. Paste and save the following, replace `<token>` with your Discord bot token:
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
            "TOKEN": "<token>"
        }
      }
    ]
  }
  ```
  * Debug the solution
