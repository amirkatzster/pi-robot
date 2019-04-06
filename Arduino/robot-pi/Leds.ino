const int CLK = 50; 
const int DIO = 52;
TM1637Display display(CLK, DIO);  //set up the 4-Digit Display.

void ledsInit() {
  display.setBrightness(0x0a);
}


void ledsLoop() {
    if (pushButtonCounter > 0 &&
        (pushButtonCounter % 7 == 0 || containsSeven(pushButtonCounter))) {
      //boom
      display.showNumberHexEx(0x800A);
      display.setBrightness(7); 
    } else {
      display.showNumberDec(pushButtonCounter); //Display the Variable value;
      display.setBrightness(2); 
    }
    
    
}

bool containsSeven(int num) {
  while (num > 0) {
    if (num % 10 == 7)
      return true;
    num /= 10;
  }
  return false;
}

