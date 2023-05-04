import csv
from decimal import Decimal

class Solution():
    def __init__(self):
        self.tempLists = []
        self.tempDict = {}
    
    def solution1(self):
        for i in range(1, 8, 2):
            space = int((7 - i) / 2)
            print(f'{space * " "}{i * "*"}{space * " "}')
        

    def solution2(self):
        sum = 0
        high = 0
        low = 0
        cnt = 0
        with open('./temperature.csv', 'r') as file:
            csvReader = csv.reader(file)
            for line in csvReader:
                tempList = []
                for temperature in line:
                    temperature = Decimal(temperature)
                    tempGrey = int(temperature * 255 / 100)
                    tempList.append(tempGrey)
                    sum += temperature
                    if (cnt == 0):
                        low = temperature
                    else:
                        if (temperature > high):
                            high = temperature
                        if (temperature < low):
                            low = temperature
                cnt += 1
                self.tempLists.append(tempList)
        
        with open('./temperatureGrey.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.tempLists)
                
        self.tempDict["high"] = high
        self.tempDict["low"] = low
        self.tempDict["avg"] = sum / cnt
        print("Highest Temperature: ", self.tempDict.get('high'))
        print("Lowest Temperature: ", self.tempDict.get('low'))
        print("Average Temperature: ", self.tempDict.get('avg'))
            