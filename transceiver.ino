#include <SPI.h>
#include <RH_RF95.h>

#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 7
#define RF95_FREQ 915.0
RH_RF95 rf95(RFM95_CS, RFM95_INT);

String inStreamString = "";
char inStreamValue;

void setup() {
  Serial.begin(57600);
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  rf95.init();
  rf95.setFrequency(RF95_FREQ);
  rf95.setTxPower(23, false);
}

void loop() {
  while(Serial.available() > 0) {
    getFromSerial(); //if present, get the data from serial coms, parse the packet, and send to radio
  }
  if (rf95.available()) {
    getFromRadio(); //if present, get the data from radio coms, and forward to serial port
  }
}

void getFromRadio() {
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);

  if (rf95.recv(buf, &len)) {
    Serial.println((char*)buf);
  } else {
    Serial.println("Receive failed");
  }
}

void getFromSerial() {
  inStreamValue = Serial.read();
  inStreamString.concat(inStreamValue);
  if(inStreamString.charAt(inStreamString.length()-1) == '~' && inStreamString.length() >= 2) {
    if(inStreamString.charAt(inStreamString.length()-2) == '~') {
      inStreamString = ""; inStreamString.concat('~'); inStreamString.concat('~'); //clear string and append packet opening tags
    }
  }
  if(inStreamString.charAt(inStreamString.length()-1) == '|' && inStreamString.length() >= 4) {
    if(inStreamString.charAt(inStreamString.length()-2) == '|' && inStreamString.charAt(0) == '~' && inStreamString.charAt(1) == '~') {
      sendData(inStreamString); //send completed packet string to radio output
    }
  }
}

void sendData(String packet) {
   char charBuf[inStreamString.length() + 5];
   inStreamString.toCharArray(charBuf, inStreamString.length()+6);
   Serial.println(charBuf);
   rf95.send((uint8_t *)charBuf, sizeof(charBuf));
   rf95.waitPacketSent();
   inStreamString = "";
}
