
import numpy as np

from data.RideReader import RideReader

from Analysis import Analysis

class SharedRides(Analysis):
    def get_driver_metrics(self):
        message = """
        Shared Rides:
        ------------------------------------------------
        Percent rides that can have shared pickups: {pickup_matching}

        """.format(pickup_matching=str(self.pickup_matching()))

        print(message)

    # group pickups by lat,long ranges, by time
    def pickup_matching(self):
        reader = RideReader(self.data_csvs[0])

        latlons_grid = {}

	# Create 'fuzzy' lat,lon,pickup_time by flooring to nearest ACCEPTABLE_PICKUP, ACCEPTABLE_TIME
        ACCEPTABLE_PICKUP = 0.003
        ACCEPTABLE_TIME = 5
        for i in range(reader.get_num_rows()):
            ride = reader.get_ride_at_index(i)

            rounded_lat, rounded_lon = ride.get_floored_pickup_lat_lon(ACCEPTABLE_PICKUP)
            rounded_pickup = ride.get_floored_pickup_mins(ACCEPTABLE_TIME)

            if rounded_lat == 0 and rounded_lon == 0:
                continue

            key = str(rounded_lat) + ',' + str(rounded_lon) + ',' + str(rounded_pickup)
            if not key in latlons_grid:
                latlons_grid[key] = []
            latlons_grid[key].append(i)

	# bucket by fuzzy computations and take ratio of (buckets.size > 1).num_rides / total_rides
        valid_shared_pickups = 0
        for k in latlons_grid.keys():
            t = latlons_grid[k]
            if len(t) > 1:
                print(k)
                valid_shared_pickups += 1

        print(valid_shared_pickups)
        print(reader.get_num_rows())
        return float(valid_shared_pickups) * 100/reader.get_num_rows()

        # problem 3
        # append destination + dropoff time in key and check > 1


