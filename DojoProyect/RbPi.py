from sense_hat import SenseHat

sense = SenseHat()

temp = sense.pressure
humidity = sense.humidity
pressure = sense.pressure


data = {
    "temp": [temp],
    "humidity": [humidity],
    "pressure": [pressure]
}

print(data)
