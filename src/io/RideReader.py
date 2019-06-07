
from models.Ride import Ride

from CsvReader import CsvReader

class RideReader(CsvReader):
    def __init__(self, fpath):
        CsvReader.__init__(self, fpath)

    def get_next_ride(self):
        row = self.get_next_row()
        return self.row_to_ride(row)

    def get_ride_at_index(self, index):
        row = self.get_row_at_index(index)
        return self.row_to_ride(row)

    def row_to_ride(self, row):
        medallion = self.get_value_for_row_col(row, 'medallion')
        pickup_datetime = self.get_value_for_row_col(row, 'pickup_datetime')
        dropoff_datetime = self.get_value_for_row_col(row, 'dropoff_datetime')
        passenger_count = self.get_value_for_row_col(row, 'passenger_count')
        trip_time_in_secs = self.get_value_for_row_col(row, 'trip_time_in_secs')
        trip_distance = self.get_value_for_row_col(row, 'trip_distance')
        pickup_longitude = self.get_value_for_row_col(row, 'pickup_longitude')
        pickup_latitude = self.get_value_for_row_col(row, 'pickup_latitude')
        dropoff_longitude = self.get_value_for_row_col(row, 'dropoff_longitude')
        dropoff_latitude = self.get_value_for_row_col(row, 'dropoff_latitude')

        return Ride(driver=medallion, pickup_datetime=pickup_datetime, dropoff_datetime=dropoff_datetime, passenger_count=passenger_count, trip_time_in_secs=trip_time_in_secs, trip_distance=trip_distance, pickup_longitude=pickup_longitude, pickup_latitude=pickup_latitude, dropoff_longitude=dropoff_longitude, dropoff_latitude=dropoff_latitude)
