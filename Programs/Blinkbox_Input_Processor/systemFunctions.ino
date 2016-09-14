boolean onTime(unsigned long *lastUpdateTime, unsigned int waitTime)
{
  if(millis() - *lastUpdateTime >= waitTime)
  {
    *lastUpdateTime = millis();
    return true;
  }
  return false;
}

void excuteFrontDistanceCheckRountine()
{
  float distance = ultrasonicSensor1.getDistance();
  if ( distance <= 300.0 && obstructionDetected == false)
  {
    obstructionDetected = true;
    //sendCommand(OBSTRUCTION_DETECTED);
    sendCommand(HORN_ON);
  }
  else if (obstructionDetected == true && distance > 300.0)
  {
    obstructionDetected = false;
    sendCommand(HORN_OFF);
  }
  else
  {
    Serial.print("Dist =");
    Serial.println(distance);
  }
}

boolean logFunction(int function, int *variables, int howmany)
{
  File myFile = SD.open("F_LOGS.LOG", FILE_WRITE);

  if (myFile)
  {
    myFile.print(function);
    myFile.print(",");
    myFile.print(howmany);
    for (int i=0; i<howmany-1; i++)
    {
      myFile.print(",");
      myFile.print(variables[i]);
      
    }
    myFile.print(",");
    myFile.println(variables[howmany-1]);
    myFile.close();
    return true;
  }
  return false;
}

void printFunctionLog()
{
  File myFile = SD.open("F_LOGS.LOG");
  if(myFile)
  {
    while(myFile.available() > 2)
    {
      int function = myFile.parseInt();
      int howmany = myFile.parseInt();
      Serial.print(function);
      Serial.print("F = ");
      for(int i=0; i<howmany; i++)
      {
        Serial.print(myFile.parseInt());
        if(i >= howmany-1)
        {
          Serial.println(";");
        }
        else
        {
          Serial.print(",");
        }
      }
    }
    myFile.close();
  }
  else
  {
    Serial.println("could not open function logs.");
  }
}

