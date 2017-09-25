import glob
import requests

def postSensorData( influxDbAddress, database, data ):

    url = influxDbAddress + "/write?db="+database

    r = requests.post(url, data)    

    if (r.status_code > 200 and r.status_code < 300):
        print "sensordata posted successfully"
    else:
        print "statuscode: " + str(r.status_code)
        print "body: " + r.text
        
    return;

def applyCorrection( sensorId, temp, factors ):

    correctedTemp = temp + factors.get(sensorId, 0)

    return correctedTemp;

# Correction table that contains a factor which must be applied to readouts for each sensor.	
corrections = { '28-051686b158ff': .35, '28-03168ca2c8ff': .075, '28-051686ea97ff': .175, '28-041685fa48ff': -0.25, '28-041694cc68ff': .125, '28-0316858728ff': .500, '28-0316859023ff': .325, '28-0316856daaff': .175, '28-0316858c69ff': .375, '28-0316858ac8ff': .0}

# Get the Id's of all onewire DS18HB2 sensors that are attached to the device.
# For each connected sensor, a file is available on the filesystem that contains the data that has been read by the sensor.
sensorids = glob.glob("/sys/devices/w1_bus_master1/28*")

query=""

for sensor in sensorids:

    print "reading " + sensor

    temp_file = open(sensor + "/w1_slave")

    info = temp_file.read()

    temp_file.close()

    templine = info.split("\n")[1]

    tempdata = templine.split(" ")[9]

    temp = float(tempdata[2:])

    temp = temp / 1000

    sensorId = sensor[sensor.find("28-"):]

    print "sensor:" + sensor + " = " + str(temp) + " gr, corrected " + str(applyCorrection(sensorId, temp, corrections))
   

    query += "sensordata,sensorid=" + sensorId + " value=" + str(temp) + "\n"


if query != "":
    postSensorData("http://localhost:8086", "heatflow", query)


