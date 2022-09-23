import csv
import socket
import sys
import os

dataPath = os.path.expanduser("~") + "/pd/data/"
fileName = "sw090522.csv"

def is_float(ele: any) -> bool:
    try:
        float(ele)
        return True
    except ValueError:
        return False

class solarWind:
    def __init__(self, time, s, d, ds, temp):
        self.timeTag = time
        self.speed = s
        self.density = d
        self.densityScaled = ds
        self.temperature = temp
    def __str__(self):
        return "Time Tag: " + self.timeTag + '\n' + "Speed: " + str(self.speed) + '\n' + "Density: " + str(self.density) + '\n' + "Temperature: " + str(self.temperature) + '\n'

swList = []

with open(dataPath + fileName, 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        if not (row):
            continue
        if not is_float(row[1]):
            continue
        swList.append(solarWind(row[0].lstrip().rstrip(), float(row[1]), float(row[2]), float(row[2]), float(row[3])))


try:
    s = socket.socket()
    print("socket successfully created")
except socket.error as e:
    print("socket creation failed with error %s" %(e))

#port = 80
port = 3000

try:
    host = socket.gethostname()
except socket.error as e:
    print('error getting host: %s' %(e))
    sys.exit()

s.connect((host, port))

print("socket successfully connected")
'''
for sw in swList:
    try:
        msgtxt = "py " + str(sw.density)
        msg = msgtxt + " ;"
        s.send(msg.encode('utf-8'))
        #i = input("Press any key to continue... ")
    except socket.error as e:
        print('error sending data: %s' %(e))
        print('unsent data: ' + sw)
'''
minD = swList[0].density
maxD = swList[0].density
for sw in swList:
    if sw.density < minD:
        minD = sw.density
    if sw.density > maxD:
        maxD = sw.density

rangeD = maxD - minD
for sw in swList:
    scaledD = 1 + (((sw.density - minD) * (48 - 1)) / rangeD)
    sw.densityScaled = scaledD

for sw in swList:
    try:
        msgtxt = "py " + str(sw.densityScaled)
        msg = msgtxt + " ;"
        s.send(msg.encode('utf-8'))
    except socket.error as e:
        print('error sending data: %s' %(e))
        print('unsent data: ' + sw)


