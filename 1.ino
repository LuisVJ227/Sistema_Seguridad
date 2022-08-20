const 
int led = 13;
int sensormg = 5;
int buzzer = 8;
int control = 7;
int val = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(control, OUTPUT);
  pinMode(led,OUTPUT);
  pinMode(sensormg, INPUT);
  pinMode (buzzer, OUTPUT);
}

void loop() 
{
  if (Serial.available()>0)
  {
    char c = Serial.read();
    if(c == 'a')
    {
      digitalWrite(7,HIGH);
    }
    else if (c == 'b')
    {
     digitalWrite(7,LOW);
    }
  }
  val = digitalRead(sensormg);
      if(val == LOW)
       {
        digitalWrite(led, HIGH);
        digitalWrite(buzzer, HIGH);
        delay(200);
        digitalWrite(led,LOW);
        digitalWrite(buzzer, LOW);
        delay(200);
       }
       else
       {
        digitalWrite(led,LOW);
        digitalWrite(buzzer,LOW);
       }
}
