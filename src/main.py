
from analyze.DriverMetrics import DriverMetrics
from analyze.SharedRides import SharedRides

print("NYC TLC taxi ride data from 2013:")

DriverMetrics(['data/trip_data/trip_data_sample_medium.csv']).get_driver_metrics()
SharedRides(['data/trip_data/trip_data_sample_medium.csv']).get_driver_metrics()
