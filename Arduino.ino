int led = 13;
int sensormg = 5;
int buzzer = 8;
int val = 0;

void setup() {
  pinMode(led,OUTPUT);
  pinMode(sensormg, INPUT);
  pinMode (buzzer, OUTPUT);
}

void loop() {
  val = digitalRead(sensormg);
  if(val == LOW){
    digitalWrite(led, HIGH);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(led,LOW);
    digitalWrite(buzzer, LOW);
    delay(200);}
  else{
    digitalWrite(led,LOW);
    digitalWrite(buzzer,LOW);
  }
}
