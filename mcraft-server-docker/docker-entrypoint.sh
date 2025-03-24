#!/bin/sh 

#Accepts EULA if var EULA has been modified in docker run (docker run -e EULA=true)
sed -i 's#eula=false#eula='"$EULA"'#g' /dockerfiles/eula.txt

#Changes level seed if var SEED has been modified in docker run (docker run -e SEED=x)
sed -i 's#level-seed=#level-seed='"$SEED"'#g' /dockerfiles/server.properties 

#Changes RCON password if var RCONPASS has been modified in docker run (docker run -e RCONPASS=x) 
sed -i 's#rcon.password=#rcon.password='"$RCONPASS"'#g' /dockerfiles/server.properties 

#Copies eula.txt and server.properties to WORKDIR (for it to work with volumes and shared folders, swarm...)
cp /dockerfiles/eula.txt /app && cp /dockerfiles/server.properties /app

# Check if server.jar exists in the destination directory
if [ ! -f "/app/server.jar" ]; then
    wget https://piston-data.mojang.com/v1/objects/4707d00eb834b446575d89a61a11b5d548d8c001/server.jar -O /app/server.jar
fi

#Starts server
java -Xms1G -Xmx2G -jar /app/server.jar nogui 
