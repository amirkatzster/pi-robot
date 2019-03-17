const int RAISE_HAND_DELAY = 3000;


void RaiseRightHand()
{
   rArmServo.write(170); 
   delay(RAISE_HAND_DELAY); 
   rArmServo.write(20); 
   delay(25);
}

void KifHands() {
   rArmServo.write(150); 
   delay(RAISE_HAND_DELAY); 
   rArmServo.write(70); 
   delay(RAISE_HAND_DELAY);
   rArmServo.write(20);
   delay(25);
}


void RaiseLeftHand()
{
   lArmServo.write(30); 
   delay(RAISE_HAND_DELAY); 
   lArmServo.write(180); 
   delay(25);
}


void RaiseBothHands()
{
   lArmServo.write(30); 
   delay(1000);
   rArmServo.write(170); 
   delay(RAISE_HAND_DELAY); 
   HandDown();
}

void HoldSomethingHands()
{
   rArmServo.write(90); 
   lArmServo.write(90); 
   delay(RAISE_HAND_DELAY * 10); 
   HandDown();
}

void HandDown()
{
   lArmServo.write(180); 
   rArmServo.write(20); 
   delay(25);
}

