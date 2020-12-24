echo off
:start 
C:\server\steamcmd\steamcmd.exe +login anonymous +force_install_dir c:\server\rustserver\ +app_update 258550 +quit
RustDedicated.exe -batchmode +server.port 28015 +server.level "Procedural Map" +server.seed 1234 +server.worldsize 4000 +server.maxplayers 10  +server.hostname "Jørgen server" +server.description "Bare for harde kjerner." +server.identity "server1" +rcon.port 28016 +rcon.password letmein +rcon.web 1