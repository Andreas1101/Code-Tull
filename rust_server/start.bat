echo off
:start 
C:\steamcmd\steamcmd.exe +force_install_dir +login anonymous c:\rustserver\ +app_update 258550 +quit
RustDedicated.exe -batchmode +server.port 28015 +server.level "Procedural Map" +server.seed 92946045 +server.worldsize 3600 +server.maxplayers 10  +server.hostname "Gulag" +server.description "Bare for harde kjerner." +server.identity "server1" +rcon.port 28016 +rcon.password letmein +rcon.web 1