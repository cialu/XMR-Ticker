/*
Luca Ciavatta (www.cialu.net)
Contact: luca.ciavatta@cialu.net

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include <LiquidCrystal.h>


LiquidCrystal lcd(2, 3, 4, 5, 6, 7); // Init LiquidCrystal with used pins
char xmr_value[15];                  // Allocate some space for the string
char inChar;                         // Where to store the character read
byte index = 0;                      // Index into array; where to store the character

// Setup the display
void setup()
{
  Serial.begin(9600);  // Setup the serial monitor
    lcd.begin(16, 2);  // Init the display
    lcd.clear();       // clear the display
    lcd.print("XMR/EUR  XMR/BTC");  // Print the title line
  
}

// Main loop
void loop(void)
{
  delay(1000);         // Set a standard delay 

if (Serial.available() > 0) {   // As long the serial connection is on
  
  index = 0;
  while (index < 14)            // One less than the size of the array
       {
           inChar = Serial.read();    // Read a character
           xmr_value[index] = inChar; // Store it
           index++;                   // Increment where to write next
       }
       Serial.flush();          // Flush the serial interface

  lcd.setCursor(1,1);           // Set cursor on the second line
  lcd.print(xmr_value);         // Print the xmr values on the second line
  Serial.println(xmr_value);    // Send back values to serial
			    }

}
