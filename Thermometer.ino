int thermistorpin = 0;
double onlyusingoneresistor = 45;
double setresist = 1000. * onlyusingoneresistor;
double c;
double temperature;
double roundedtemperature;
double resist;
int laston = 0;
int redpin = 10;
int greenpin = 12;
int bluepin = 11;
double measuredvoltage;
double hightemp = 56.;
double lowtemp = 18.;
double avgsamples()          //Take average of 10 thermistor readings to reduce effect of outliers
{
    int maxind, minind;
    double sum = 0.;
    int numdeleted;
    double maxread = -1.;
    double minread = 1024.;
    int const NUMBEROFSAMPLES = 10;
    int selection[NUMBEROFSAMPLES];
    for (int i = 0; i < NUMBEROFSAMPLES; i++)
    {
        selection[i] = analogRead(thermistorpin);
        if (selection[i] > maxread)
            maxread = selection[i];
        if (selection[i] < minread)
            minread = selection[i];
        delay(100);
    }
    for (int j = 0; j < NUMBEROFSAMPLES; j++)
    {
        if (selection[j] == maxread)
        {    selection[j] = -1;
             break;
        }
    }
    for (int ja = 0; ja < NUMBEROFSAMPLES; ja++)
    {
        if (selection[ja] == minread)
        {    selection[ja] = 1024;
             break;
        }
    }
    for (int k = 0; k < NUMBEROFSAMPLES; k++)
    {
        if ((-1 < selection[k]) && (selection[k] < 1024))
            sum += selection[k];
    }
    return (sum / (NUMBEROFSAMPLES - 2));
}
double larryconversion(double reading)   //Implement regression equation calculated for the device
{
    return pow(reading, 5) * (-0.0167973656) + pow(reading, 4) * (0.3964290003) +  pow(reading, 3) * (-4.3590818278) + pow(reading, 2) * (20.8091075982) + reading * (-60.6340975474) + (116.7382716864);
}
void setup()  //Setup serial ports for LED'd
{
    Serial.begin(9600);
    pinMode(redpin, OUTPUT);
    pinMode(bluepin, OUTPUT);
    pinMode(greenpin, OUTPUT);
}
void loop()    //main program
{
    //report temperature based on thermistor's readings
    c = avgsamples();
    measuredvoltage = ((((c*10)-(int) c % 10)/10)/1023.) * 5.;
    temperature = larryconversion(measuredvoltage);
    temperature *= 10.;
    temperature = round(temperature);
    roundedtemperature = temperature / 10.;
    //resist = (setresist * c) / (1023 - c);
    //Serial.print(resist); Serial.print(" ");
    //Serial.print(c); Serial.println(" ");
    Serial.print("Voltage: "); Serial.print(measuredvoltage); Serial.print("  ");  Serial.print("Temperature in Degrees Celsius: "); Serial.println(roundedtemperature);

    //LED control
    //LED control; if temp is low turn on red, if temp is medium, turn on green, if temp is high, turn on blue; red is default

    if(roundedtemperature <= lowtemp)
    {
        if(laston != 0)
            digitalWrite(laston, LOW);
        digitalWrite(redpin, HIGH);
        laston = redpin;
    }
    else if (hightemp >= roundedtemperature && roundedtemperature > lowtemp)
    {
        if(laston != 0)
              digitalWrite(laston, LOW);
        digitalWrite(greenpin, HIGH);
        laston = greenpin;
    }
    else if (hightemp < roundedtemperature)
    {
        if(laston != 0)
            digitalWrite(laston, LOW);
        digitalWrite(bluepin, HIGH);
        laston = bluepin;
    }
    else
    {
        if(laston != 0)
            digitalWrite(laston, LOW);
        digitalWrite(redpin, HIGH);
        laston = redpin;
    }
}
