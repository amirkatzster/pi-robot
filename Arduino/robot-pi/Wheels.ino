

void TurnRight()
{
   digitalWrite(in1, LOW);
   digitalWrite(in2, HIGH);
   delay(2000);
   digitalWrite(in1, LOW);
   digitalWrite(in2, LOW);
}


void TurnLeft()
{
   digitalWrite(in3, HIGH);
   digitalWrite(in4, LOW);
   delay(2000);
   digitalWrite(in3, LOW);
   digitalWrite(in4, LOW);
}

void MoveFw()
{
   digitalWrite(in3, HIGH);
   digitalWrite(in4, LOW);
   digitalWrite(in1, LOW);
   digitalWrite(in2, HIGH);
   delay(2000);
   digitalWrite(in3, LOW);
   digitalWrite(in4, LOW);
   digitalWrite(in1, LOW);
   digitalWrite(in2, LOW);
}

void MoveBw()
{
   digitalWrite(in3, LOW);
   digitalWrite(in4, HIGH);
   digitalWrite(in1, HIGH);
   digitalWrite(in2, LOW);
   delay(2000);
   digitalWrite(in3, LOW);
   digitalWrite(in4, LOW);
   digitalWrite(in1, LOW);
   digitalWrite(in2, LOW);
}
