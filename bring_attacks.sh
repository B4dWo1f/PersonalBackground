#!/bin/bash

USER="n03l"
DOMAIN="kasterborous.ddns.net"
#ssh $USER@$DOMAIN "apps/SSH_watcher/plot_attacks.py "
#scp -P1210 n03l@kasterborous.ddns.net:attacks.png .
scp $USER@$DOMAIN:attacks.png $HOME/Pictures/background/
ssh $USER@$DOMAIN "rm attacks.png"
inkscape --export-png=$HOME/Pictures/background.png $HOME/apps/background/background.svg
