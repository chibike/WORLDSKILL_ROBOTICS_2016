#ifdef INCLUDE_COMPASS
void runCompassCheckRountine()
{
  int16_t prevXacc  = 0;
  int16_t prevYacc  = 0;
  int16_t prevZacc  = 0;
  boolean forward   = false;
  uint8_t variables[] = {200, 0x00, 0x0A};
  pause_MCU2_I2C();
  myCompass.lockTarget();
  continue_MCU2_I2C();

  sendCommand(SET_EXCUTE_FUNCTION);
  while(1)
  {
    if(forward == false)
    {
      forward = true;
      sendCommand(MCU_2_I2C_ADDRESS, FD_COMMAND, variables, 3);
    }
    else
    {
      forward = false;
      sendCommand(MCU_2_I2C_ADDRESS, BD_COMMAND, variables, 3);
    }
    delay(200);
    pause_MCU2_I2C();delay(200);
    int16_t xAcc  = myCompass.getAccX();delay(200);
    int16_t yAcc  = myCompass.getAccY();delay(200);
    int16_t zAcc  = myCompass.getAccZ();delay(200);
    int8_t  pitch = myCompass.getPitch();delay(200);
    int8_t  roll  = myCompass.getRoll();delay(200);
    int16_t temp  = myCompass.getTemp();delay(200);
    
    Serial.println("************************");
    printFloat("Heading = ", myCompass.getHeading());
    printInt16("xAcc = ", xAcc);
    printInt16("yAcc = ", yAcc);
    printInt16("zAcc = ", zAcc);
    printInt16("pitch = ", pitch);
    printInt16("roll = ", roll);
    printInt16("temp = ", temp);
    printInt16("AngleError = ", myCompass.getTargetDeviation());
    printInt16("xAccError = ", prevXacc-xAcc);
    printInt16("yAccError = ", prevYacc-yAcc);
    printInt16("zAccError = ", prevZacc-zAcc);

    prevXacc  = xAcc;
    prevYacc  = yAcc;
    prevZacc  = zAcc;

    continue_MCU2_I2C();
    sendCommand(MCU_2_I2C_ADDRESS, STOP_COMMAND, variables, 0);
    
    delay(100);
  }
}

void printInt16(char* str, int16_t val)
{
  Serial.print(str);
  Serial.println(val);
  delay(100);
}

void printFloat(char* str, float val)
{
  Serial.print(str);
  Serial.println(val);
  delay(100);
}
#endif
