#
# Luca Ciavatta (www.cialu.net)
# Contact: luca.ciavatta@cialu.net
#
# /home/pi/xmr-startup.sh
#
# screen -dmS <title> <command>

screen -dmS monero-node bash -c '/home/pi/monero/monerod --rpc-bind-ip=192.168.xxx.xxx --rpc-bind-port=xxxx --confirm-external-bind'
screen -dmS xmr-ticker bash -c '/usr/bin/python3 /home/pi/xmr-ticker.py'

