//// MOTORS //////////
const int enA = 6;
const int enB = 7;
const int in1 = 22;
const int in2  = 24;
const int in3 = 26;
const int in4  = 28;
//////////////////////


void wheelsInit() {
  ///MOTORS//////////
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  //////////////////
}

void wheelsReset() {
   digitalWrite(in1, LOW);
   digitalWrite(in2, LOW);
   digitalWrite(in3, LOW);
   digitalWrite(in4, LOW);
}

void TurnLeft(int speed)
{
   Stop();
   SetSpeed(speed,speed);
   digitalWrite(in1, LOW);
   digitalWrite(in2, HIGH);
}


void TurnRight(int speed)
{
   Stop();
   SetSpeed(speed,speed);
   digitalWrite(in3, HIGH);
   digitalWrite(in4, LOW);
}

void MoveFw(int speed)
{
   Stop();
   SetSpeed(speed,speed - 50);
   digitalWrite(in3, HIGH);
   digitalWrite(in4, LOW);
   digitalWrite(in1, LOW);
   digitalWrite(in2, HIGH);
}

void MoveBw(int speed)
{
   Stop();
   SetSpeed(speed,speed);
   digitalWrite(in3, LOW);
   digitalWrite(in4, HIGH);
   digitalWrite(in1, HIGH);
   digitalWrite(in2, LOW);
}

void Stop()
{
   digitalWrite(in3, LOW);
   digitalWrite(in4, LOW);
   digitalWrite(in1, LOW);
   digitalWrite(in2, LOW);
}

void SetSpeed(int speedL,int speedR) {
   analogWrite(enA, speedL);
   analogWrite(enB, speedR);
}

