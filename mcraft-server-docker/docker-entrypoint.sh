#!/bin/sh 

#Accepts EULA if var EULA has been modified in docker run (docker run -e EULA=true)
sed -i 's#eula=false#eula='"$EULA"'#g' /app/eula.txt

#Changes level seed if var SEED has been modified in docker run (docker run -e SEED=x)
sed -i 's#level-seed=#level-seed='"$SEED"'#g' /app/server.properties 

#Starts server
java -Xms1G -Xmx2G -jar server.jar nogui 