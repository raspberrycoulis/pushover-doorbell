//////////////////////////////////////////////////
// ESP8266 Pushover message on button push      //
// Button is connected between GND and D2 GPIO  //
//////////////////////////////////////////////////

#include <ESP8266WiFi.h>

// Button
int buttonState = 0;


// Pushover
String Token  = "ADD_HERE";
String User   = "ADD_HERE";
int length;

//  WiFi
WiFiClient client;
const char* ssid     = "ADD_HERE";
const char* password = "ADD_HERE";

// Setup
void setup() {
  Serial.begin(115200);
  pinMode(D2, INPUT_PULLUP);

  // WiFi setup
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA); //Client mode only
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print("_");
  }
  Serial.println("");
  Serial.print(ssid);
  Serial.println(" successfully connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  delay(50);
}

void loop() {
  buttonState = digitalRead(D2);

    if (buttonState == LOW) {
      pushover("Somebody is at the door!");
      Serial.println("Somebody is at the door!");
      delay(5000);
    }
  }


byte pushover(char *pushovermessage) {
 
  String Msg = pushovermessage;
  length = 113 + Msg.length();
    if (client.connect("api.pushover.net", 80)) {
      client.println("POST /1/messages.json HTTP/1.1");
      client.println("Host: api.pushover.net");
      client.println("Connection: close\r\nContent-Type: application/x-www-form-urlencoded");
      client.print("Content-Length: ");
      client.print(length);
      client.println("\r\n");
      client.print("token="+Token+"&user="+User+"&title=Doorbell&sound=doorbell-3&message="+Msg);
      /* Uncomment this to receive a reply from Pushover server:*/
      /*while(client.connected()) {
        while(client.available()) {
          char ch = client.read();
          Serial.write(ch);
        }
      }*/
      client.stop();
    }
}
