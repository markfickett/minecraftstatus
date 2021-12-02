#!/usr/bin/env python3
# Proxy the Minecraft server status response. This makes the status detailing
# which players are online easily available as a JSON response via HTTP.
from mcstatus import GetJson
from mcstatus import DEFAULT_PORT

# Add a file mcstatusproxyconfig.py for your Minecraft server, which defines:
#     HOST = 'myserver.com'
from mcstatusproxyconfig import HOST

import json
import socket


if __name__ == '__main__':
  print('Content-Type: application/json\r\n\r')
  resp = {}
  try:
    raw_json = GetJson(HOST, DEFAULT_PORT)
    # Only include player status (and not the icon etc).
    resp['players'] = raw_json.get('players')
  except (socket.error, ValueError) as e:
    pass
  print(json.dumps(resp))
