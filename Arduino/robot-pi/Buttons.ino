/////PUSH BUTTON//////
const int pushButtonRed  = 23;
//////////////////////


int pushButtonCounter = 0;
int lastButtonState = 0; 


void buttonsInit() {
  pinMode(pushButtonRed, INPUT_PULLUP);
}

void readButton() {
  int buttonValue = digitalRead(pushButtonRed);
  if (buttonValue == LOW && lastButtonState != buttonValue){
      // If button pushed, turn LED on
      Serial.println(pushButtonCounter++);
      delay(50);
  } else {
      // Otherwise, turn the LED off
      //digitalWrite(LED, LOW);
  }
  lastButtonState = buttonValue;
}


