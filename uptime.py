import os

from rcon.source import Client
from dotenv import load_dotenv

load_dotenv(override=True)



with Client(os.getenv("RCON_HOST"), int(os.getenv("RCON_PORT")),
  passwd=os.getenv("RCON_PASSWORD")) as client:
      response = client.run('players')

print(response)