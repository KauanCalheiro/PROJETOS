#include <VarSpeedServo.h> // adiciona biblioteca do servo motor
const int  buttonPin = 2; //botao - pino 2
int buttonState = 0; 

// laranja fosco - comum
// branco - botao pro lado do braco
// laranja brilhante - botao pro lado oposto do braco -- nao precisa usar

VarSpeedServo myservo; 
void setup()
{
  pinMode(buttonPin, INPUT_PULLUP); // define pino alto quando nao tem sinal negativo
  myservo.attach(9);  //  motor - pino 9
  myservo.write(0,255);
  myservo.wait();
    Serial.begin(19200); // habilita leitura da porta
}

void loop()
{
  Serial.println (digitalRead(buttonPin)); // faz leitura da porta 2
  buttonState = digitalRead(buttonPin);  // Le posicao do botao
  if (buttonState == 0) // executa comando quando receber sinal negativo/GND
  {
    switch (random(1, 3))// seleciona modo aleatorio
    {
      case 1:
        myservo.write(100, 200);
        myservo.wait();
        myservo.write(0, 200);
        myservo.wait();
      break;
      case 2:
        myservo.write(50, 200);
        myservo.wait();
        myservo.write(100, 230);
        myservo.wait();
        myservo.write(0, 230);
      break;
      case 3:
        myservo.write(100, 250);
        myservo.wait();
        myservo.write(80, 100);
        myservo.wait();
        delay(2000);
        myservo.write(0, 50);
        myservo.wait();
      break;
    }
  }
}
