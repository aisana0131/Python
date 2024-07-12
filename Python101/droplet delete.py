import os
from pydo import Client

connection = Client(token=os.getenv("DO_TOKEN"))

sshKeyName = "AisanaSSH"

ssh_keys = connection.ssh_keys.list()
print(ssh_keys)

for key in ssh_keys['ssh_keys']:
    if sshKeyName == key['module-droplet']:
       

new_droplet = connection.droplets.create(body)
print(new_droplet)