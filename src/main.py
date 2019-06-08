
# from analyze.DriverMetrics import DriverMetrics
from analyze.SharedRides import SharedRides

shared_rides = SharedRides(['../data/trip_data/trip_data_sample_medium.csv'])
shared_rides.get_driver_metrics()
