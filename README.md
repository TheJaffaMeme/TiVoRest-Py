# TiVoRest-Py
A really really really basic and simple rest api server thing to send commands to tivo boxes

# Requirements
Python 3 with the supplied requirements.txt

# Config
Inside config.json you have "TIVOIP", "TIVOPORT", "HTTPIP" and "HTTPPORT"

Config Option | Explanation
------------ | -------------
"TIVOIP" | The IP of the TiVo box you want to control (default is x.x.x.x) - This is the most important part of config
"TIVOPORT" | The port the TiVo box uses for control (default is 31339)
"HTTPIP" | The IP the web server will use (default is 0.0.0.0)
"HTTPPORT" | The port the webserver will use (default is 5000)

# Endpoints

Endpoint | Value | Explanation
------------ | - | -------------
/IRCODE?value= | [An IRCODE] | You can find a list at https://community.home-assistant.io/t/control-tivo-box-over-telnet/12430] - Sends a remote control command
/SETCH?value= | [A channel number] | Sets the channel to given channel number
/STATUS | N/A | Responds with the current channel number

All of these are done as GET, really sorry I can't explain this further I just don't have the right knowledge. It'll always give back a 200 ok.

# Please Keep In Mind
I made this for my own little projects and thought it might be useful to someone. It might not work for other boxes and the code is utter shit.
