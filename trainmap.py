


class Station:
    def __init__(self,name):
        self._name = name
        self._neighbours = []
    def getName(self):
        return self._name
    
    def addNeighnour(self,station):
        self._neighbours.append(station)
    
    def getNeighnours(self):
        return self._neighbours
    
class TrainMap:
    def __init__(self):
        self._stations = {}
        print("train map created ")
    
    def addstation(self,stationName):
        self._stations[stationName] = Station(stationName)
        return self
    def getStation(self,stationname):
        return self._stations[stationname]
    
    def connectStations(self,fromstation,tostation):
        fromstation.addNeighnour(tostation)
        tostation.addNeighnour(fromstation)
        return self
    def shortestPath(self,source,destination):
        print("inside shortest path function----")
        source_station = self.getStation(source)
        dest_station = self.getStation(destination)
        print("source_station is",source_station)
        print("destination station is", dest_station)
        print("self.stations is",self._stations)





def drivercode():
    trainmap = TrainMap()
    trainmap.addstation("KCST").addstation("Angel").addstation("oldstreet").addstation("Moorgate").addstation("Farrington")\
    .addstation("barbican").addstation("Russelsquare").addstation("Holdborn").addstation("Chancery").addstation("St.Pauls").addstation("Bank")
    
    trainmap.connectStations(trainmap.getStation("KCST"),trainmap.getStation("Angel"))\
    .connectStations(trainmap.getStation("KCST"),trainmap.getStation("Farrington"))\
    .connectStations(trainmap.getStation("KCST"),trainmap.getStation("Russelsquare"))\
    .connectStations(trainmap.getStation("Russelsquare"),trainmap.getStation("Holdborn"))\
    .connectStations(trainmap.getStation("Holdborn"),trainmap.getStation("Chancery"))\
    .connectStations(trainmap.getStation("Chancery"),trainmap.getStation("St.Pauls"))\
    .connectStations(trainmap.getStation("St.Pauls"),trainmap.getStation("Bank"))\
    .connectStations(trainmap.getStation("Angel"),trainmap.getStation("oldstreet"))\
    .connectStations(trainmap.getStation("oldstreet"),trainmap.getStation("Moorgate"))\
    .connectStations(trainmap.getStation("Moorgate"),trainmap.getStation("Bank"))\
    .connectStations(trainmap.getStation("Farrington"),trainmap.getStation("barbican"))\
    .connectStations(trainmap.getStation("barbican"),trainmap.getStation("Moorgate"))\
  
    trainmap.shortestPath("KCST","St.Pauls")


