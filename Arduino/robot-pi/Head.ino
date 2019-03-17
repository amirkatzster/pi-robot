const int SERVO_NO_DELAY = 800;
const int SERVO_YES_DELAY = 1200;

void SayYes()
{
   yesServo.write(155); 
   delay(SERVO_YES_DELAY); 
   yesServo.write(130); 
   delay(SERVO_YES_DELAY); 
   yesServo.write(160); 
   delay(SERVO_YES_DELAY);
   yesServo.write(140);
   delay(SERVO_YES_DELAY);
}

void SayNo()
{
   noServo.write(160); 
   delay(SERVO_NO_DELAY); 
   noServo.write(50); 
   delay(SERVO_NO_DELAY); 
   noServo.write(160); 
   delay(SERVO_NO_DELAY);
   noServo.write(95);
   delay(SERVO_NO_DELAY);
}


void LookRight()
{
   noServo.write(20); 
   delay(SERVO_NO_DELAY * 4); 
   noServo.write(95);
   delay(SERVO_NO_DELAY);
}


void LookLeft()
{
   noServo.write(160); 
   delay(SERVO_NO_DELAY * 4); 
   noServo.write(95);
   delay(SERVO_NO_DELAY);
}

void Search()
{
   for (int i = 0; i < 3; i++) {
     int noServoMove = random(70, 120);
     int yesServoMove = random(100, 160);
     noServo.write(noServoMove); 
     delay(SERVO_NO_DELAY); 
     yesServo.write(yesServoMove); 
     delay(SERVO_YES_DELAY); 
   }
   noServo.write(95);
   delay(SERVO_NO_DELAY); 
   yesServo.write(140);
   delay(SERVO_YES_DELAY);
   

}
