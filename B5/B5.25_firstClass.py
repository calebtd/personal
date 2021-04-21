class Flight:
    def __init__(self, flight_num, city_source, city_dest, num_passengers,
                 num_attendants, depart_dt, flight_dur):
        """Flight number, source city, destination city, number of passengers,
        number of flight attendants, departure date and time, flight duration"""
        self.flight_num = flight_num
        self.city_source = city_source
        self.city_dest = city_dest
        self.num_passengers = num_passengers
        self.num_attendants = num_attendants
        self.depart_dt = depart_dt
        self.flight_dur = flight_dur


if __name__ == '__main__':
    flight = Flight(2597, 'SLC', 'LAX', 338, 6, '04/20/2021 13:45', '01:03')
