
#include <Servo.h>
#include <Wire.h>
#include <TM1637Display.h>
#define SLAVE_ADDRESS 0x04


Servo yesServo;  // create servo object to control a servo
Servo noServo;
Servo rArmServo;
Servo lArmServo;



int number = 0;
int action = 0; //1 - sayYes, 2 - sayNo
bool once;

void setup() {
  once = true;
  Serial.begin(9600);
  // TALK WITH PI ////////
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
  /////////////////////

  headInit();
  wheelsInit();
  buttonsInit();
  ledsInit();
 
}

void Reset() {
  /// Head ///
   yesServo.write(140);
   noServo.write(95);
   rArmServo.write(20);
   lArmServo.write(180);
   /// Wheels ///
   wheelsReset();
}



void loop() { 
 
 if (once) {
  once = false;
//  LookRight();
//  RaiseRightHand();
//  RaiseLeftHand();  
 }
 if (action > 0)  {
  Serial.print(" I received:");
  Serial.println(action);
  commitAction(action);
  action = -1;
 }
 readButton();
 ledsLoop();
}




void commitAction(int action) {
  switch (action) {
    case 0:
      Reset();
      break;
    case 1:
      SayYes();
      break;
    case 2:
      SayNo();
      break;
    case 3:
      LookRight();
      break;
    case 4:
      LookLeft();
      break;
    case 5:
      Search();
      break;
    case 50:
      RaiseRightHand();   
      break;
    case 51:
      RaiseLeftHand();
      break;
    case 52:
      RaiseBothHands();
      break;
    case 53:
      HoldSomethingHands();
      break;
    case 54:
      KifHands();
      break;
    case 71:
      MoveFw(240);
      break;
    case 72:
      MoveBw(240);
      break;
    case 73:
      TurnRight(255);
      break;
    case 74:
      TurnLeft(255);
      break;
    case 75:
      Stop();
      break;
    default:
      break;
  }
}



void receiveData(int byteCount) {
  Serial.print("receiveData: ");
  while (Wire.available()) {
    number = Wire.read();
    Serial.println(number);
    action = number;
  }
}
void sendData() {
  Serial.print("respond with number: ");
  Serial.println(number);
  Wire.write(number);
}







