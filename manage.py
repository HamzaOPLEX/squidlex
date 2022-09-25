# this script need admin privilege for using docker commands :)

import docker
import os

container_name = 'SquidProxy'
save_commands = [
    'chown -R squid:squid /var/squidGuard',
    'squidGuard -C all',
    'squid -k reconfigure',
    'service squid restart',
]

# Create image
# Pull image

# Create the Container
def dockerCompose():
    os.popen("docker compose up -d").read()

# Run Command in the container
def dockerExec():
    for cmd in save_commands:
        print(os.popen(f"docker exec -d {container_name} {cmd}").read())

dockerExec()