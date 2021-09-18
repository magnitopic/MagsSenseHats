from sense_hat import SenseHat

sense = SenseHat()

# We'll print the value we recive
print("Humidity: "+str(sense.humidity))
print("Temperature: "+str(sense.temp))
print("Presure: "+str(sense.pressure))
