from model import model as BusLineModel

busLineModel = BusLineModel()
busLinesData = busLineModel.readJson_File()

BusID = "132路"
BusStop = "朝陽科技大學"

def findBus():

    for bus in busLinesData:
        if bus[busLineModel.BusLineID] == BusID:
            print(bus)


def findStop():

    for bus in busLinesData:
        if BusStop in bus[busLineModel.RoundTrip_ob].split("停靠：")[1].split("、") or BusStop in bus[busLineModel.RoundTrip_ib].split("停靠：")[1].split("、"):
            print(bus[busLineModel.BusLineID])

# findBus()
findStop()