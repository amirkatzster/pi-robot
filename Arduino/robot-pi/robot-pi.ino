
#include <Servo.h>
#include <Wire.h>
#define SLAVE_ADDRESS 0x04


Servo yesServo;  // create servo object to control a servo
Servo noServo;
Servo rArmServo;
Servo lArmServo;

///////HEAD Setup ///////

const int servoPinYes = 5;
const int servoPinNo = 4;
const int servoRightArm = 3;
const int servoLeftArm = 2;
int servoStartingAngle = 90;
int servoOpenAngle = 180;
///////////////////////
//// MOTORS //////////
const int enA = 6;
const int enB = 7;
const int in1 = 22;
const int in2  = 24;
const int in3 = 26;
const int in4  = 28;
//////////////////////
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

  ///HEAD ////////////
  yesServo.attach(servoPinYes); 
  noServo.attach(servoPinNo); 
  rArmServo.attach(servoRightArm); 
  lArmServo.attach(servoLeftArm); 
  Reset(); 
  ////////////////////

  ///MOTORS//////////
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  //////////////////
}

void Reset() {
  /// Head ///
   yesServo.write(140);
   noServo.write(95);
   rArmServo.write(20);
   lArmServo.write(180);
   /// Wheels ///
   digitalWrite(in1, LOW);
   digitalWrite(in2, LOW);
   digitalWrite(in3, LOW);
   digitalWrite(in4, LOW);
}



void loop() { 
  /*
  if (Serial.available() > 0) {
    char income = Serial.read(); // read the incoming byte:
    Serial.print(" I received char:");
    Serial.print(income);
    action = atoi(&income);
    //action = income;
    Serial.print(" I received:");
    Serial.println(action);
  }
  */
 
 
 if (once) {
  once = false;
  LookRight();
  RaiseRightHand();
  RaiseLeftHand();  
 }
 if (action > 0)  {
  Serial.print(" I received:");
  Serial.println(action);
  commitAction(action);
  action = -1;
 }
 
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
      MoveFw(155);
      break;
    case 72:
      MoveBw(155);
      break;
    case 73:
      TurnRight(155);
      break;
    case 74:
      TurnLeft(155);
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







