class Map():
    def __init__(self, username, carinfo):
        self.username = username
        self.carinfo = carinfo
    
    def startinfo(self, map_start, start_time):
        self.map_start = map_start
        self.start_time = start_time

    def arriveinfo(self, map_arrive, arrive_time):
        self.map_arrive = map_arrive
        self.arrive_time = arrive_time
    
    def gas_station_info(self, gas_station, station_arrive_time):
        self.gas_station = gas_station
        self.station_arrive_time = station_arrive_time
        if self.start_time > station_arrive_time or station_arrive_time > self.arrive_time:
            print("Error: 출발시간과 도착시간 사이에 주유소에 도착 불가능")
            self.station_arrive_time = "시간안에 못감. 도착지로 바로 직행."

    def printing_destination_info(self):
        print(f"출발지: {self.map_start}시 \n경유지: {self.gas_station} \n목적지: {self.map_arrive} \n총 걸리는 시간: {self.arrive_time-self.start_time}
              ")