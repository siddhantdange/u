
import numpy as np

from data.RideReader import RideReader

from Analysis import Analysis

class DriverMetrics(Analysis):
    def get_driver_metrics(self):
        print(self.avg_trips_per_hour_per_driver())
        print('done!')

    def avg_trip_lengths(self):
        reader = RideReader(self.data_csvs[0])
        distances = reader.get_col_iter('trip_distance')

        return np.median(distances)

    def avg_trips_per_hour_per_driver(self):
        reader = RideReader(self.data_csvs[0])

        driver_to_hours = {}
        for i in range(reader.get_num_rows()):
            ride = reader.get_ride_at_index(i)
            if ride.driver not in driver_to_hours:
                driver_to_hours[ride.driver] = {}

            if ride.pickup_datetime.hour not in driver_to_hours[ride.driver]:
                driver_to_hours[ride.driver][ride.pickup_datetime.hour] = {
                    'count': 0,
                    'days': set()
                }

            driver_to_hours[ride.driver][ride.pickup_datetime.hour]['count'] += 1

            ymd = ride.get_pickup_day_str()
            if not ymd in driver_to_hours[ride.driver][ride.pickup_datetime.hour]['days']:
                driver_to_hours[ride.driver][ride.pickup_datetime.hour]['days'].add(ymd)


        hour_averages = {}
        for hour in list(range(24)):
            hour_averages[hour] = []

        for driver in driver_to_hours.keys():
            for hour in driver_to_hours[driver].keys():
                hour_avg = float(driver_to_hours[driver][hour]['count'])/len(driver_to_hours[driver][hour]['days'])
                hour_averages[hour].append(hour_avg)

        hour_average = {}
        for hour in hour_averages.keys():
            hour_average[hour] = sum(hour_averages[hour])/len(hour_averages[hour])

        return hour_average

