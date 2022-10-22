# eVisionTech-Testwork

## Running

Run the command
> docker compose up

## Requirements

- Docker v20.*
- Was tested on Ubuntu 20.04

## Configuring

To configure target path go to /dirview_service/config.py and alterate "path" variable.
Since the task does not specify the need to work with internal or external file system paths both approaches has been implemented using outer/OS filesystem mounted to /outerspace path. 