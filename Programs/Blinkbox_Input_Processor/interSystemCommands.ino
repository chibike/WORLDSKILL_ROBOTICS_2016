void pause()
{
  sendCommand(PAUSE);
  onPause = true;
}

void play()
{
  sendCommand(CONTINUE);
  onPause = false;
}

void pause_MCU2_I2C()
{
  Wire.beginTransmission(MCU_2_I2C_ADDRESS);
  Wire.write(PAUSE_I2C);
  Wire.endTransmission(MCU_2_I2C_ADDRESS);
}

void continue_MCU2_I2C()
{
  Wire.beginTransmission(MCU_2_I2C_ADDRESS);
  Wire.write(CONTINUE_I2C);
  Wire.endTransmission(MCU_2_I2C_ADDRESS);
}

bool changeLane(bool side, bool avoidObstacles)
{
  
}

void sendCommand(byte address, uint8_t command)
{
  if (i2cBusy == false)
  {
    pause_MCU2_I2C();
    
    Wire.beginTransmission(address);
    Wire.write(command);
    Wire.endTransmission(address);

    continue_MCU2_I2C();
  }
  else
  {
    queue_I2C_command(command);
  }
}

void sendCommand(uint8_t command)
{
  if (i2cBusy == false)
  {
    pause_MCU2_I2C();
    Wire.beginTransmission(MCU_2_I2C_ADDRESS);
    Wire.write(command);
    Wire.endTransmission(MCU_2_I2C_ADDRESS);
    continue_MCU2_I2C();
  }
  else
  {
    queue_I2C_command(command);
  }
}

void sendCommand(byte address, uint8_t command, uint8_t *variables, uint16_t howmany)
{
  if (i2cBusy == false)
  {
    pause_MCU2_I2C();
    
    Wire.beginTransmission(address);
    Wire.write(command);
    for(int i=0; i<howmany; i++)
    {
      Wire.write(variables[i]);
    }
    Wire.endTransmission(MCU_2_I2C_ADDRESS);

    continue_MCU2_I2C();
  }
  else
  {
    queue_I2C_command(command, variables, howmany);
  }
}

void sendCommand(uint8_t command, uint8_t *variables, uint16_t howmany)
{
  if (i2cBusy == false)
  {
    pause_MCU2_I2C();
    
    Wire.beginTransmission(MCU_2_I2C_ADDRESS);
    Wire.write(command);
    for(int i=0; i<howmany; i++)
    {
      Wire.write(variables[i]);
    }
    Wire.endTransmission(MCU_2_I2C_ADDRESS);

    continue_MCU2_I2C();
  }
  else
  {
    queue_I2C_command(command, variables, howmany);
  }
}

void queue_I2C_command(uint8_t command)
{
  int variables[0];
  int n = 0;
  myFunctionsQueue.insertFunction(command, variables, n);
}

void queue_I2C_command(uint8_t command, uint8_t *variables, uint16_t howmany)
{
  /*------- NOTE -------*/
  /*
   * function = command;
   * variables = array(variables);
   * l = len(variables);
   * variables = cat(l, variables);
   * #therefore variables[0] == len(variables)-1;
   * QueueFunction(function, variables)
   */
  int vars[howmany+1];
  vars[0] = (int)howmany;
  for(int i=0; i>howmany; i++)
  {
    vars[i+1] = (int)variables[i];
  }
  myFunctionsQueue.insertFunction(command, vars, howmany);
}

void sendQueued_I2C_commands()
{
  /*------- NOTE ----------*/
  /*
   * Function Storage Structure
   * array(FUNC1, FUNC2, FUNC...); for functions
   * array(VAR_COUNT_2, VAR1, VAR2, VAR_COUNT_N, VAR1, VAR2, VAR..);
   * Therefore the first variable tells the number of variables required
   * for that function.
   */
  
  while ( i2cBusy == false && myFunctionsQueue.isEmpty() == false )
  {
    uint8_t command;
    int howmany;
    if( myFunctionsQueue.getNextFunction(&command) == false )
    {
      return;
    }
    else if( myFunctionsQueue.getNextVariable(&howmany) == false )
    {
      sendCommand(command);
      return;
    }
    else if(howmany <= 0)
    {
      sendCommand(command);
      return;
    }
    uint8_t variables[howmany];
    for(int i=0; i<howmany; i++)
    {
      int variable; 
      if( myFunctionsQueue.getNextVariable(&variable) == true )
      {
        variables[i] = (uint8_t)variable;
      }
      else
      {
        return;
      }
    }
    
    sendCommand(command, variables, howmany);
  }
}

