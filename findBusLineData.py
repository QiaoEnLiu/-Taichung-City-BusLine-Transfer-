from model import model as BusLineModel

busLineModel = BusLineModel()
busLinesData = busLineModel.readJson_File()

BusID = "132路"
BusStop = "朝陽科技大學"

takeStop = "朝陽科技大學"
desStop = "逢甲大學(福星路)"

CYUT = "朝陽科技大學"
FCU_FSR = "逢甲大學(福星路)"
NTUT = "國立臺中科技大學"

def findBus(BusID):

    for bus in busLinesData:
        if bus[busLineModel.BusLineID] == BusID:
            print(bus[busLineModel.BusLineID], bus[busLineModel.BusLineName], bus[busLineModel.Com_BusLine], sep = "\n")
            print(busLineModel.RoundTrip_ob, bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、"), sep = ":")
            print(busLineModel.RoundTrip_ib, bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、"), sep = ":")
            print("--------------")


def findStop(stop):
    stopData = []
    for bus in busLinesData:
        if stop in bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、") or stop in bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、"):
            '''
            print(bus[busLineModel.BusLineID], bus[busLineModel.BusLineName], bus[busLineModel.Com_BusLine], sep = "\n")
            print(busLineModel.RoundTrip_ob, bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、"), sep = ":")
            print(busLineModel.RoundTrip_ib, bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、"), sep = ":")
            print("--------------")
            '''


            tempDict = {busLineModel.BusLineID: bus[busLineModel.BusLineID],
                        busLineModel.RoundTrip_ob: bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、"),
                        busLineModel.RoundTrip_ib: bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、")
                        }
            stopData.append(tempDict)

    return stopData


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


            tempDict = {busLineModel.BusLineID: bus[busLineModel.BusLineID],
                        busLineModel.BusLineName: bus[busLineModel.BusLineName],
                        busLineModel.Com_BusLine: bus[busLineModel.Com_BusLine],
                        busLineModel.RoundTrip_ob: ob_Temp[ob_Temp.index(stopName):] if stopName in ob_Temp else [],
                        busLineModel.RoundTrip_ib: ib_Temp[ib_Temp.index(stopName):] if stopName in ib_Temp else []
                        }
            stopData.append(tempDict)
    return stopData

# findBus("15繞1路")

# desStopData = findStop(desStop)
# takeStopData = findStop(takeStop)

startStop = startTakeStop(NTUT)


for busLine in startStop:
    print(busLine[busLineModel.BusLineID], busLine[busLineModel.BusLineName], busLine[busLineModel.Com_BusLine], sep = "\n")
    print(busLineModel.RoundTrip_ob, busLine[busLineModel.RoundTrip_ob], sep = ":")
    print(busLineModel.RoundTrip_ib, busLine[busLineModel.RoundTrip_ib], sep = ":")
    print("--------------")
    