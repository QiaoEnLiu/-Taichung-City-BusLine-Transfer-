from model import model as BusLineModel

busLineModel = BusLineModel()
busLinesData = busLineModel.readJson_File()


CYUT = "朝陽科技大學"
FCU_FSR = "逢甲大學(福星路)"
NTUT = "國立臺中科技大學"

def startTakeStop(stopName):
    stopData = []
    for bus in busLinesData:
        ob_Temp = []
        ib_Temp = []

        is_In_ob = stopName in bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、")
        is_In_ib = stopName in bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、")

        if is_In_ob or is_In_ib:
            ob_Temp = bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、")
            ib_Temp = bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、")

            # ['A Stop', 'B Stop', 'C Stop', 'D Stop', 'E Stop']
            # 路線[路線.index(撘乘站):]
            # <=================== take C <--------------------- 由撘乘站至可下車站 <==
            # -------------------> take C =====================> 由撘乘站至可下車站 ==>
            tempDict = {busLineModel.BusLineID: bus[busLineModel.BusLineID],
                        busLineModel.BusLineName: bus[busLineModel.BusLineName],
                        busLineModel.Com_BusLine: bus[busLineModel.Com_BusLine],
                        busLineModel.RoundTrip_ob: ob_Temp[ob_Temp.index(stopName):] if stopName in ob_Temp else [],
                        busLineModel.RoundTrip_ib: ib_Temp[ib_Temp.index(stopName):] if stopName in ib_Temp else []
                        }
            stopData.append(tempDict)
    return stopData


def endDesStop(stopName):
    stopData = []
    for bus in busLinesData:
        ob_Temp = []
        ib_Temp = []

        is_In_ob = stopName in bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、")
        is_In_ib = stopName in bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、")

        if is_In_ob or is_In_ib:
            ob_Temp = bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、")
            ib_Temp = bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、")

            # ['A Stop', 'B Stop', 'C Stop', 'D Stop', 'E Stop']
            # 路線[:路線.index(目的地站) + 1]
            # =====================> take C ---------------------> 至目的地可撘乘站 ==>
            # <--------------------- take C <===================== 至目的地可撘乘站 <==
            
            tempDict = {busLineModel.BusLineID: bus[busLineModel.BusLineID],
                        busLineModel.BusLineName: bus[busLineModel.BusLineName],
                        busLineModel.Com_BusLine: bus[busLineModel.Com_BusLine],
                        busLineModel.RoundTrip_ob: ob_Temp[:ob_Temp.index(stopName) + 1] if stopName in ob_Temp else [],
                        busLineModel.RoundTrip_ib: ib_Temp[:ib_Temp.index(stopName) + 1] if stopName in ib_Temp else []
                        }
            stopData.append(tempDict)
    return stopData

takeStopName = input("撘乘站({})：".format(CYUT)) or CYUT
print("---------------", f"你的撘乘站：{takeStopName}", "---------------", sep = '\n')
desStopName = input("目的地({})：".format(FCU_FSR)) or FCU_FSR
print("---------------", f"你的目的地：{desStopName}", "---------------", sep = '\n')


desStopData = endDesStop(desStopName)
takeStopData = startTakeStop(takeStopName)

takeTo_List = []
toDes_List = []



for takeBus in takeStopData:
    for desBus in desStopData:
        if set(takeBus[busLineModel.RoundTrip_ob]).isdisjoint(desBus[busLineModel.RoundTrip_ob]) and \
            set(takeBus[busLineModel.RoundTrip_ob]).isdisjoint(desBus[busLineModel.RoundTrip_ib]) and \
            set(takeBus[busLineModel.RoundTrip_ib]).isdisjoint(desBus[busLineModel.RoundTrip_ob]) and \
            set(takeBus[busLineModel.RoundTrip_ib]).isdisjoint(desBus[busLineModel.RoundTrip_ib]):
            pass
        else:

            '''
            print(takeBus[busLineModel.BusLineID], desBus[busLineModel.BusLineID])
            print(set(takeBus[busLineModel.RoundTrip_ob]) & set(desBus[busLineModel.RoundTrip_ob]))
            print(set(takeBus[busLineModel.RoundTrip_ob]) & set(desBus[busLineModel.RoundTrip_ib]))
            print(set(takeBus[busLineModel.RoundTrip_ib]) & set(desBus[busLineModel.RoundTrip_ob]))
            print(set(takeBus[busLineModel.RoundTrip_ib]) & set(desBus[busLineModel.RoundTrip_ib]))
            print("--------------")
            '''

            if takeBus not in takeTo_List:
                takeTo_List.append(takeBus)
            if desBus not in toDes_List:
                toDes_List.append(desBus)

print(f"{takeStopName} 前往 {desStopName} 需要轉乘", "---------------", sep = '\n')

print("可撘乘的公車：", "------", sep = '\n')

for takeBus in takeTo_List:
    print(takeBus[busLineModel.BusLineID])

print("---------------")
selectTakeBus = input("選擇撘乘公車：") or takeTo_List[0][busLineModel.BusLineID]
print("---------------", f"你所選擇的公車：{selectTakeBus}", "---------------", sep = '\n')
print("可轉乘的公車：", "------", sep = '\n')

for takeBus in takeTo_List:
    if takeBus[busLineModel.BusLineID] == selectTakeBus:
        selectTakeBusLine = takeBus

transferToDes_List = []
for desBus in desStopData:
    if set(selectTakeBusLine[busLineModel.RoundTrip_ob]).isdisjoint(desBus[busLineModel.RoundTrip_ob]) and \
        set(selectTakeBusLine[busLineModel.RoundTrip_ob]).isdisjoint(desBus[busLineModel.RoundTrip_ib]) and \
        set(selectTakeBusLine[busLineModel.RoundTrip_ib]).isdisjoint(desBus[busLineModel.RoundTrip_ob]) and \
        set(selectTakeBusLine[busLineModel.RoundTrip_ib]).isdisjoint(desBus[busLineModel.RoundTrip_ib]):
        pass
    else:
        print(desBus[busLineModel.BusLineID])
        '''
        print(selectTakeBusLine[busLineModel.BusLineID], desBus[busLineModel.BusLineID])
        print(set(selectTakeBusLine[busLineModel.RoundTrip_ob]) & set(desBus[busLineModel.RoundTrip_ob]))
        print(set(selectTakeBusLine[busLineModel.RoundTrip_ob]) & set(desBus[busLineModel.RoundTrip_ib]))
        print(set(selectTakeBusLine[busLineModel.RoundTrip_ib]) & set(desBus[busLineModel.RoundTrip_ob]))
        print(set(selectTakeBusLine[busLineModel.RoundTrip_ib]) & set(desBus[busLineModel.RoundTrip_ib]))
        print("--------------")
        '''
        if desBus not in transferToDes_List:
            transferToDes_List.append(desBus)


print("---------------")
selectTF_Bus = input("選擇轉乘公車：") or transferToDes_List[0][busLineModel.BusLineID]
print("---------------", f"你所選擇的轉乘公車：{selectTF_Bus}", "---------------", sep = '\n')

print(f"由{selectTakeBus}轉乘{selectTF_Bus}可在以下站點轉乘：", "------", sep = '\n')


for desBus in desStopData:
    for takeBus in takeStopData:
        if takeBus[busLineModel.BusLineID] == selectTakeBus and desBus[busLineModel.BusLineID] == selectTF_Bus:
            if set(takeBus[busLineModel.RoundTrip_ob]).isdisjoint(desBus[busLineModel.RoundTrip_ob]) and \
                set(takeBus[busLineModel.RoundTrip_ob]).isdisjoint(desBus[busLineModel.RoundTrip_ib]) and \
                set(takeBus[busLineModel.RoundTrip_ib]).isdisjoint(desBus[busLineModel.RoundTrip_ob]) and \
                set(takeBus[busLineModel.RoundTrip_ib]).isdisjoint(desBus[busLineModel.RoundTrip_ib]):
                pass
            else:
                print([stop for stop in takeBus[busLineModel.RoundTrip_ob] if stop in desBus[busLineModel.RoundTrip_ob]])
                print([stop for stop in takeBus[busLineModel.RoundTrip_ob] if stop in desBus[busLineModel.RoundTrip_ib]])
                print([stop for stop in takeBus[busLineModel.RoundTrip_ib] if stop in desBus[busLineModel.RoundTrip_ob]])
                print([stop for stop in takeBus[busLineModel.RoundTrip_ib] if stop in desBus[busLineModel.RoundTrip_ib]])


            