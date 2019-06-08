
import numpy as np

from data.RideReader import RideReader

from Analysis import Analysis

class DriverMetrics(Analysis):
    def get_driver_metrics(self):
        message = """
        Driver Metrics:
        ------------------------------------------------
        Average trips length: {avg_trip_length}

        Average trips per hour over all drivers: {avg_trips_per_hour}

        Average driver utilization: {avg_driver_util}

        """.format(avg_trip_length=str(self.avg_trip_lengths()), avg_trips_per_hour=self.avg_trips_per_hour_per_driver(), avg_driver_util=self.get_avg_driver_util())

        print(message)

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

    # util = all_trip_durations/(last_start_day - first_start_day).to_s
    def get_avg_driver_util(self):
        reader = RideReader(self.data_csvs[0])

        driver_trip_durations = {}
        for i in range(reader.get_num_rows()):
            ride = reader.get_ride_at_index(i)
            if ride.driver not in driver_trip_durations:
                driver_trip_durations[ride.driver] = {
                    'total_d': 0,
                    'first': ride.pickup_datetime,
                    'last': ride.pickup_datetime
                }

            driver_trip_durations[ride.driver]['total_d'] += ride.trip_time_in_secs
            if ride.pickup_datetime < driver_trip_durations[ride.driver]['first']:
                driver_trip_durations[ride.driver]['first'] = ride.pickup_datetime

            if ride.pickup_datetime > driver_trip_durations[ride.driver]['last']:
                driver_trip_durations[ride.driver]['last'] = ride.pickup_datetime

        total_util = 0
        num_valid_drivers = 0

        utils = []
        for driver in driver_trip_durations.keys():
            duration_data = driver_trip_durations[driver]

            if driver_trip_durations[driver]['first'] == driver_trip_durations[driver]['last']:
                continue

            utils.append(float(duration_data['total_d'])/(duration_data['last'] - duration_data['first']).total_seconds())

        return np.median(utils)

