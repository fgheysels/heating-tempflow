# heating-tempflow
This is a simple project that allows me to tune my underfloor-heating system.  
I want to measure the temperature of the water that flows in and out of every circuit of the heating system.
This information will be used to tune each circuit so that the inflow-temperature of each circuit is equal to 
the others.
This should result in a better balanced temperature throughout the house, and hopefully a lower gas bill.

Python scripts are used to read out sensor-output of multiple DS18B2 temperature-sensors that are measuring
the in- and outflow temperature of all the underfloor-heating circuits that are present in the house.

The sensor-data is submitted to an InfluxDB timeseries database and Grafana is used to visualize the data.
Using this information allows me to make sure that the inflow-water temperature for all heating-circuits are
evenly divided

Everything runs on a Raspberry Pi.

# DS18B2 sensors

the DS18B2 sensor is a 1-wire sensor that is able to measure temperatures between -50°C to +125°C.
Multiple sensors can be connected in parallel.
A 4.7k ohm resistor is necessary between the data and the VCC wire:

>Another feature of the DS18B20 is the ability to operate
>without an external power supply. Power is instead
>supplied through the 1-Wire pullup resistor through the
>DQ pin when the bus is high. The high bus signal also
>charges an internal capacitor (CPP), which then supplies
>power to the device when the bus is low. This method of
>deriving power from the 1-Wire bus is referred to as “parasite
>power.” As an alternative, the DS18B20 may also be
>powered by an external supply on VDD.

See the wiring scheme below:

![Screenshot](doc/wiring_schema.png "DS18B2 wiring schema for Raspberry Pi 3")
