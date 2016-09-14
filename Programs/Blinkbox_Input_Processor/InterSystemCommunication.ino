#define PAUSE_I2C 22
#define CONTINUE_I2C 23

void RECEIVE_EVENT(int howmany)
{
  int buffer = Wire.read();
  if (buffer == PAUSE_I2C)
  {
    i2cBusy = true;
  }
  else if (buffer == CONTINUE_I2C)
  {
    i2cBusy = false;
  }
  else if(buffer == LOG_FUNCTION)
  {
    int function = Wire.read();
    int howmany  = Wire.read();
    int variables[howmany];
    for(int i=0; i<howmany; i++)
    {
      variables[i] = Wire.read();
    }
    logFunction(function, variables, howmany);
  }
}

void REQUEST_EVENT()
{
  //pass
}
