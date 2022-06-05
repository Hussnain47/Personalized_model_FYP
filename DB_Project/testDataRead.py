import json
import matplotlib.pyplot as plt

def ReadJson(filename):
    with open(filename, "r") as file:
        return json.loads(file.read())

Heart = ReadJson("data_heart.json")["bucket"]
Sleep = ReadJson("data_sleep.json")["bucket"]
# Steps = ReadJson("data_Steps.json")["bucket"]

exactStart = 1649438039497

nanosToMillis = (10**6)
millisToSec = (10**3)
millisToMin = (60*millisToSec)
millisToHours = (60*millisToMin)

def getData(obj, instance = False, val = 'intVal'):
    # if instance:
        instances = obj["dataset"][0]["point"]
        rtn = []
        for i in instances:
            start = ((int(i["startTimeNanos"])/nanosToMillis)-exactStart)/millisToHours
            end = ((int(i["endTimeNanos"])/nanosToMillis)-exactStart)/millisToHours
            dif = end-start
            Value = i["value"][0][val]
            rtn.append((start, end, dif, Value))
        return rtn
    # c = 1000*60*60*24
    # start = int(obj["startTimeMillis"])/c
    # end = int(obj["endTimeMillis"])/c
    # dif = end-start
    # return start, end, dif



H = getData(Heart[0], True, 'fpVal')
Sl = getData(Sleep[0], True)
# St = getData(Steps[0], True)

# lenHeartData, lenSleepData = len(H), len(Sl)
TimeFactor = 1

HeartTime = [x[1] for x in H if x[1]<H[-1][1]//TimeFactor]
# print(HeartTime)
SleepTime = [x[1] for x in Sl if x[1]<=HeartTime[-1]]
# same = len(set(HeartTime).intersection(set(SleepTime)))
# print("same:", same, '\nHeart:', len(HeartTime), '\nSleep:', len(SleepTime))
HeartData = [x[-1] for x in H][:len(HeartTime)]
SleepData = [x[-1] for x in Sl][:len(SleepTime)]

print(*Sl, sep="\n")
# print(SleepTime[1])

# plt.bar(HeartTime, HeartData, 0.1, color='green')
# plt.show()
# plt.scatter(SleepTime, SleepData,  color= 'red')
# plt.show()
# plt.bar([x[1] for x in St], [x[-1] for x in St],80)
# plt.show()