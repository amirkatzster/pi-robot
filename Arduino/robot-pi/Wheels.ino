

void TurnLeft(int speed)
{
   SetSpeed(speed);
   digitalWrite(in1, LOW);
   digitalWrite(in2, HIGH);
}


void TurnRight(int speed)
{
   SetSpeed(speed);
   digitalWrite(in3, HIGH);
   digitalWrite(in4, LOW);
}

void MoveFw(int speed)
{
   SetSpeed(speed);
   digitalWrite(in3, HIGH);
   digitalWrite(in4, LOW);
   digitalWrite(in1, LOW);
   digitalWrite(in2, HIGH);
}

void MoveBw(int speed)
{
   SetSpeed(speed);
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

void SetSpeed(int speed) {
   analogWrite(enA, speed);
   analogWrite(enB, speed);
}

