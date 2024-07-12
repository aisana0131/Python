import os
from pydo import Client

client = Client(token=os.getenv("DIGITALOCEAN_TOKEN"))
