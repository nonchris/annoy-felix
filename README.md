# discord-bot-template
Generic, functional bot based on discord.py  
Including a custom help command and ping command, utils for easy embed creation, logging configuration, and a general bot setup

## setup
` python3 -m pip install -e .`  
`export TOKEN="your-key"`  
`discord-bot`

#### optional env variables
| parameter |  description |
| ------ |  ------ |
| `export PREFIX="b!"`  | Command prefix |
| `export VERSION="unknown"` | Version the bot is running |
| `export OWNER_NAME="unknwon"` | Name of the bot owner |
| `export OWNER_ID="100000000000000000"` | ID of the bot owner |
| `export ACTIVITY_NAME=f"{PREFIX}help"`| Activity bot plays |  

The shown values are the default values that will be loaded if nothing else is specified.  
Expressions like `{PREFIX}` will be replaced by during loading the variable and can be used in specified env variables.  

## features
This bot does 'nothing' but is completely functional!  
_What is does:_  
* setup logging
* scan env variables for a more customizable behaviour
* overwrite `on_ready()` function for information at startup
* make bot react to custom prefix and mention
* add more advanced help command
* register example cog with `b!ping` command
* util functions for easy embed creation, id extraction and more

Note:  
The bot uses all intents by default, those are required for such simple things like 'display member-count at startup'.  
You need to enable those intents in the discord developers portal under "Application/Bot/Privileged Gateway Intents".  
It's possible reconfigure the requested intents in `main.py` if you don't need them.  
But I'd suggest using them all for the beginning, especially if you're relatively new to discord.py.

## about
This repository contains code that was written by me across various bot-projects, like:  
https://github.com/nonchris/discord-fury  
https://github.com/nonchris/quiz-bot  
https://github.com/Info-Bonn/poll-bot

I collected the most useful and generic functions to save me some time when starting the next bot-project.

### documentation
In order to render this documentation, just call `doxygen`
