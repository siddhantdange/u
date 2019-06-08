
from datetime import datetime

class Ride():
    def __init__(self, driver, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude):
        self.driver = driver
        self.pickup_datetime = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S')
        self.dropoff_datetime = datetime.strptime(dropoff_datetime, '%Y-%m-%d %H:%M:%S')
        self.passenger_count = int(passenger_count)
        self.trip_time_in_secs = int(trip_time_in_secs)
        self.trip_distance = float(trip_distance)
        self.pickup_longitude = float(pickup_longitude)
        self.pickup_latitude = float(pickup_latitude)
        self.dropoff_longitude = float(dropoff_longitude)
        self.dropoff_latitude = float(dropoff_latitude)

    def get_mins_since_midnight(self, d):
        return d.hour * 60 + d.minute

    def get_pickup_mins(self):
        return self.get_mins_since_midnight(self.pickup_datetime)

    def get_dropoff_mins(self):
        return self.get_mins_since_midnight(self.dropoff_datetime)

    def get_ymd_str(self, date):
        return str(date).split(' ')[0]

    def get_pickup_day_str(self):
        return self.get_ymd_str(self.pickup_datetime)

    def get_dropoff_day_str(self):
        return self.get_ymd_str(self.dropoff_datetime)

    def get_floored_num(self, num, mod):
        num_dec = str(num)[::-1].find('.')

        rounded_num = num
        if num_dec > 0:
            rounded_num = num * (10**num_dec)

        mod_dec = str(mod)[::-1].find('.')
        scaled_mod = mod
        if mod_dec > 0:
            scaled_mod = mod * (10**mod_dec)

        rounded_num = rounded_num - (rounded_num % scaled)

        if num_dec > 0:
            rounded_num = rounded_num/(10**num_dec)

        return rounded_num

    def __str__(self):
        attr_dict = {
            'driver': self.driver,
            'pickup_datetime': self.pickup_datetime,
            'dropoff_datetime': self.dropoff_datetime,
            'passenger_count': self.passenger_count,
            'trip_time_in_secs': self.trip_time_in_secs,
            'trip_distance': self.trip_distance,
            'pickup_longitude': self.pickup_longitude,
            'pickup_latitude': self.pickup_latitude,
            'dropoff_longitude': self.dropoff_longitude,
            'dropoff_latitude': self.dropoff_latitude
        }

        return str(attr_dict)
