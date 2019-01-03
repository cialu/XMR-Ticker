#
# Luca Ciavatta (www.cialu.net)
# Contact: luca.ciavatta@cialu.net
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

#
# Import libs
#

import os
import sys
import serial
import time
import signal

import urllib.request
import json

#
# Set the serial interface
#

PORT = '/dev/ttyUSB0'   # Could be different like /dev/ttyS0
SPEED = 9600            # Set speed connection

connection = serial.Serial( PORT,  SPEED, timeout=0, stopbits=serial.STOPBITS_TWO)  # Init the serial connection

#
# Main loop
#

while True:
	try:
		urleur = 'https://api.cryptonator.com/api/ticker/xmr-eur'                           # API for xmr-eur
		urlbtc = 'https://api.cryptonator.com/api/ticker/xmr-btc'                           # API for xmr-btc
		resulteur = json.loads(urllib.request.urlopen(urleur).read().decode('utf-8'))       # Load eur json
		tickereur = resulteur["ticker"]                                                     # Read json keys
		priceeur = tickereur["price"]                                                       # Read json keys
		resultbtc = json.loads(urllib.request.urlopen(urlbtc).read().decode('utf-8'))       # Load btc json
		tickerbtc = resultbtc["ticker"]                                                     # Read json keys
		pricebtc = tickerbtc["price"]                                                       # Read json keys
		print ("XMR/EUR", "  ", "XMR/BTC")                                                  # Print title bar
                price = str(' ' + priceeur[:-6] + '  ' + pricebtc[:-4])                             # Stripe results
		print (price)                                                                       # Print striped results
		connection.write(price.encode())                                                    # Encode and send results to serial interface
		time.sleep(10)                                                                      # Perform a delay
	except Exception as inst:	                                                            # Caught exceptions
        	print (inst); time.sleep(30)                                                        # Print errors
		
		
