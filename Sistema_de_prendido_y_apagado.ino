const 
int led = 13;
int sensormg = 5;
int buzzer = 8;
int val = 0;
int estado = 0;
int Dato = 0;

void setup() 
{
  Serial.begin(9600);
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
      estado = 1;
    }
    else if (c == 'b')
    {
      estado = 0;
    }
  }
 
  val = digitalRead(sensormg);
  if (estado == 1)
  {
      if(val == 0)
       {
        digitalWrite(led, HIGH);
        digitalWrite(buzzer, HIGH);
        delay(200);
        digitalWrite(led,LOW);
        digitalWrite(buzzer, LOW);
        delay(200);
        Serial.println(val);
        delay(200);
       }
      
      else
       {
          digitalWrite(led,LOW);
          digitalWrite(buzzer,LOW);
          Serial.println(val);
          delay(200);
       }
  }
  else
   {
    digitalWrite(led,LOW);
    digitalWrite(buzzer,LOW);
   } 
}
