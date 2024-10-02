from model import model as BusLineModel

busLineModel = BusLineModel()
busLinesData = busLineModel.readJson_File()

BusID = "132路"
BusStop = "朝陽科技大學"

takeStop = "朝陽科技大學"
desStop = "逢甲大學(福星路)"

def findBus():

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

# findBus()
# findStop()

desStopData = findStop(desStop)
takeStopData = findStop(takeStop)