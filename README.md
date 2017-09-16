# heating-tempflow
This is a simple project that allows me to tune my underfloor-heating system.  

Python scripts are used to read out sensor-output of multiple DS18HB2 temperature-sensors that are measuring
the in- and outflow temperature of all the underfloor-heating circuits that are present in the house.

The sensor-data is submitted to an InfluxDB timeseries database and Grafana is used to visualize the data.
Using this information allows me to make sure that the inflow-water temperature for all heating-circuits are
evenly divided

Everything runs on a Raspberry Pi.
