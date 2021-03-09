int analogVal1 = 0;
float analogPIN_1_voltage;
int analogVal2 = 0;
float analogPIN_2_voltage;
//float R1 = 10000; // value of R1 on board
//float logR2, R2, T;
//float c1 = 0.001129148, c2 = 0.000234125, c3 = 0.0000000876741; //steinhart-hart coeficients for thermistor

void setup() {
Serial.begin(9600);
}

void loop() {
analogVal1 = analogRead(A0); // this signal will be plotted
analogPIN_1_voltage = analogVal1 *(5.0/1023.0);
analogVal2 = analogRead(A1); // this signal will be plotted
analogPIN_2_voltage= analogVal2 *(10.0/1023.0);
//R2 = R1 * (1023.0 / (float)analogVal2 - 1.0); //calculate resistance on thermistor
//logR2 = log(R2);
//T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2)); // temperature in Kelvin
//T = T - 273.15; //convert Kelvin to Celcius
Serial.print(analogPIN_1_voltage);
Serial.print(" , ");
Serial.println(analogPIN_2_voltage);
delay(1000);
}
