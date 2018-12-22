
#include <Servo.h>
#include <Wire.h>
#define SLAVE_ADDRESS 0x04


Servo yesServo;  // create servo object to control a servo
Servo noServo;
Servo rArmServo;

///////HEAD Setup ///////
const int SERVO_NO_DELAY = 800;
const int SERVO_YES_DELAY = 1000;
const int servoPinYes = 9;
const int servoPinNo = 6;
const int servoRightArm = 5;
int servoStartingAngle = 90;
int servoOpenAngle = 180;
///////////////////////
int number = 0;
int action = 0; //1 - sayYes, 2 - sayNo

void setup() {
  Serial.begin(9600);
  // TALK WITH PI ////////
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
  /////////////////////

  ///HEAD ////////////
  yesServo.attach(servoPinYes); 
  yesServo.write(140);
  noServo.attach(servoPinNo); 
  noServo.write(95);
  rArmServo.attach(servoRightArm); 
  rArmServo.write(0);
  ////////////////////
}



void loop() { 
 delay(100);
 SayNo();
 delay(100);
 MoveRightArm();
 switch (action) {
    case 1:
      SayYes();
      action = 0;
      break;
    case 2:
      SayNo();
      action = 0;
      break;
    default:
      break;
  }
}

void MoveRightArm()
{
   rArmServo.write(0); 
   delay(1000); 
   rArmServo.write(180); 
   delay(1000); 
   rArmServo.write(90); 
   delay(1000);
}


void receiveData(int byteCount) {
  Serial.print("receiveData");
  while (Wire.available()) {
    number = Wire.read();
    Serial.print("data received: ");
    Serial.println(number);
    if (number == 1) {
      Serial.println("Say yes");
      action = 1;
      delay(2000);
    } else {
      Serial.println("Say no");
      action = 2;
      delay(2000);
    }
  }
}
void sendData() {
  Serial.print("respond with number: ");
  Serial.println(number);
  Wire.write(number);
}

void SayYes()
{
   yesServo.write(160); 
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






