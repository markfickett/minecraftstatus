"""Check the status (availability, logged-in players) on a Minecraft server.

Usage:
    %(prog)s host [port]

Closely based on:
    https://github.com/FunnyItsElmo/PHP-Minecraft-Server-Status-Query .
"""

import argparse
import logging
import socket

DEFAULT_PORT = 25565


class McServer:

  def __init__(self, host, port=DEFAULT_PORT):
    self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self._socket.connect((host, port))
    self._sorted_players = tuple()
    self._online = False

  def Update(self):
    raise NotImplementedError()

  @property
  def online(self):
    return self._online

  @property
  def players(self):
    return tuple(self._sorted_players)


if __name__ == '__main__':
  logging.basicConfig(
      format='%(levelname)s %(asctime)s %(filename)s:%(lineno)s: %(message)s',
      level=logging.DEBUG)

  parser = argparse.ArgumentParser()
  parser.add_argument('--port', type=int, default=DEFAULT_PORT)
  parser.add_argument('host')
  args = parser.parse_args()

  logging.info('querying %s:%d', args.host, args.port)

  server = McServer(args.host, port=args.port)
  server.Update()
  logging.info('logged in players: %s', ', '.join(server.players))
