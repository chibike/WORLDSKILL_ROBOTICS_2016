#include <CMPS11_COMPASS.h>
#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <RFID_SLO30.h>
#include <Ultrasonic.h>
#include <FunctionsQueue.h>

#define I2C_ADDRESS         7
#define MCU_2_I2C_ADDRESS   8
#define PULL_2_START        0

#define STOP_COMMAND              0
#define F_COMMAND                 1
#define B_COMMAND                 2
#define FD_COMMAND                3
#define BD_COMMAND                4
#define RFD_COMMAND               5
#define RBD_COMMAND               6
#define STANDBY                   7
#define PAUSE                     8
#define CONTINUE                  9
#define SET_STEER_ANGLE          10
#define SET_WHEEL_POWER          11
#define LEFT_INDICATOR           12
#define RIGHT_INDICATOR          13
#define ONE_WAY_INDICATOR        14
#define HEAD_LIGHTS_ON           15
#define HEAD_LIGHTS_OFF          16
#define HORN_ON                  17
#define HORN_OFF                 18
#define WARNING_1                19
#define WARNING_2                20
#define WARNING_3                21
#define FOLLOW_LINE              22
#define MOVE                     23
#define ALIGN_WITH_LINE          24
#define SWAP_LANE                25
#define PAUSE_I2C                26
#define CONTINUE_I2C             27
#define WAIT                     28
#define OPEN_GRIPPER             29
#define CLOSE_GRIPPER            30
#define POBJ_COMMAND             31
#define DOBJ_COMMAND             32
#define CGPR_COMMAND             33
#define OGPR_COMMAND             34
#define LOG_FUNCTION             46
#define SET_EXCUTE_FUNCTION      47
#define RESET_EXCUTE_FUNCTION    48
#define STARTED                  49
#define NO_COMMAND               50

#define PAUSE                     4
#define CONTINUE                  5

#ifdef PULL_2_START
  #define PULL_2_START_PIN        0
#endif

bool onPause = false;
bool i2cBusy = false;
bool obstructionDetected = false;


Ultrasonic     ultrasonicSensor1(A0, 3, "mm");
RFID_SLO30     myRfidReader(B1010000, 2);
FunctionsQueue myFunctionsQueue(10, 200, 0, 0, -1,
                                210, 600, 0, 0, -2);
CMPS11_COMPASS myCompass(0x60);

void setup() 
{
  Serial.begin(115200);
  Serial.println("Started...");

#ifdef PULL_2_START
  pinMode(PULL_2_START_PIN, INPUT_PULLUP);
#endif
  myRfidReader.begin();
  myFunctionsQueue.begin();
  myCompass.begin();
  
  //myFunctionsQueue.reset();
  
  Wire.begin(I2C_ADDRESS);
  Wire.setTimeout(1000);
  Wire.onReceive(RECEIVE_EVENT);
  Wire.onRequest(REQUEST_EVENT);
  sendCommand(STARTED);
  
#ifdef PULL_2_START
  sendCommand(SET_EXCUTE_FUNCTION);
#else
  sendCommand(SET_EXCUTE_FUNCTION);
#endif
}

void loop()
{
  static unsigned long checkFrontDistanceLastUpdateTime = millis();

#ifdef PULL_2_START
  if( digitalRead(PULL_2_START_PIN) == HIGH )
  {
    sendCommand(SET_EXCUTE_FUNCTION);
  }
#endif

  if( onTime(&checkFrontDistanceLastUpdateTime, 1000) )
  {
    excuteFrontDistanceCheckRountine();
  }
  
  if( i2cBusy == false && myFunctionsQueue.isEmpty() == false )
  {
    sendQueued_I2C_commands();
  }
}
