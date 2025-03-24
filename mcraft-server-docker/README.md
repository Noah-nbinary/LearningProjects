Hello! TLDR: minecraft server image prepared for running in network drive and docker swarm, created for learning purposes only. RCON-CLI included.

Variables are: EULA=[true/false] , SEED=[seednum] and RCONPASS=[pass]
This image works with a minecraft server that runs on a NAS or shared folder (check entrypoint script)

Although not ideal, it was created to test availability through Docker Swarm and multiple nodes, for them to have the same world 
Aditional Disclaimer: Bind mounts and network drives are not ideal for this scenarios, this was for learning purposes and testing docker capabilities

In my case, it was tested with the following service config:

docker service create -t -d --name mcraftservice -e EULA=true -p 25565:25565 --mount type=bind,src=/mnt/SambaShared/Server/MinecraftVolume,dst=/app noahnbinary/mcraftserver:latest

Or with docker run: 

docker run -dit --rm --name mcraft -e EULA=true -e RCONPASS=mypass -p 25565:25565 -v /mnt/SambaShared/Server/MinecraftVolume:/app noahnbinary/mcraftserver:latest

RCON-CLI usage:

docker exec -it [container-name] rcon-cli --password [mypass] [minecraft-server-command]

The docker image and files can be found below:
https://hub.docker.com/r/noahnbinary/mcraftserver
https://github.com/Noah-nbinary/LearningProjects/tree/main/mcraft-server-docker