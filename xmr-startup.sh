#
# Luca Ciavatta (www.cialu.net)
# Contact: luca.ciavatta@cialu.net
#
# /home/pi/xmr-startup.sh
#
# screen -t <title> <tab-index> <command>

screen -t monero-node  0 forever /home/pi/monero/monerod
screen -t xmr-ticker   1 forever python3 /home/pi/xmr-ticker.py
