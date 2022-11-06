import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def makeGraph():
    y = [65, 70, 80, 63, 72, 55, 60, 80, 70]
    conditions = ["clear", "sunny", "clear", "clear", "rainy", "rainy", "clear", "sunny", "sunny"]
    x = [0,3,6,9,12,15,18,21,24]
    plt.plot(x, y)
    plt.xticks(x)
    plt.ylabel("temp in fahrenheit")
    plt.xlabel("time of day")
    plt.title("Today's Weather")
    imgPath = "../../code-quantum-weather-app/src/images/dailyWeather.png"
    plt.savefig(imgPath)
    plt.close()
    return imgPath

