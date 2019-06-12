
# Uber Crazy Taxi
## Background
In 2014, through a FOIL request, NYC TLC release a dataset containing trip data throughout 2013, containing medallion, pickup and dropoff locations, and timestamps.

This repo provides scripts analyze these trips in New York City, and will print out analytics to STDOUT

## Setup
### Download data
1. Download the compressed data from here:

https://archive.org/download/nycTaxiTripData2013/trip_data.7z

https://archive.org/download/nycTaxiTripData2013/trip_fare.7z

2. Unzip the trip_data and trip_fare compressed folders and move the csv's into the corresponding location to `data/trip_data/` and `data/trip_fare/`

3. Generate data samples, assumes downloaded data is in proper location as per 'Step 2'
`./generate_small_medium_data_samples.sh`

### Dependencies
You will need python 2.7 to run these scripts and `pip` to install the dependencies

#### Install
```
source env/bin/activate
pip install -r requirements.txt
```

## Usage
Run at root of repo: `./run_analytics.sh`

*Be sure to use this script as the entrypoint to running the application*

# Analysis
## Driver metrics:
1. Trip length - simple median of all trip durations in seconds
2. Trips/hour for drivers - computed the number of rides in each hour per day, computed the average ride per hour per driver, and averaged among all drivers
3. Average util - computed `total_ride_duration/(last_ride.start - first_ride.start)` as util per day, averaged for all days over all drivers

Other interesting metrics (per uber feature):
1. Surge pricing
    1. Avg # of passengers/hr in a day
    2. min/max trip lengths throughout day
    3. Popular pick up and drop off per day
2. Driver
    1. Avg $/hour or $/mile per hour
    2. hours when drivers get most tips
    3. % trips have tolls?
    4. % trips with tips
    5. Drivers with most tips/hour
    6. Avg service fee?

## Pickup Matching
1. Computed 'fuzzy' lat,lon for each trip by flooring to closest 0.5 mile (~0.003 in lat,lon), and did the same for pickup time. Bucketed all rides that match the same (fuzz_lat, fuzz_long, fuzz_pickup_time), and took ratio of (bucket.num_rides > 1).num_rides / total_rides

## Trip Matching
1. Same algorithm as `Pickup Matching`, except also using fuzzy dropoff lat,lon,pickup as part of bucket key

# Further work
I created a few sample of the dataset of 'small' and 'medium' size, and used jupyter notebooks + pandas to do initial analytics. In the interest of time, I chose to reuse much of the code I wrote, and created convenient abstractions that could be extended for other metrics.

Had there been more time, I would have done the following for a development solution -
1. Use postgreSql for aggregations, let query planner handle optimizing paging + memory
2. Preprocess data, create indicies on driver, since many of the calculations involve aggregations per-driver
3. Create separate table for fuzzy lat,lon,pickup,dropoff data
4. Drop cancelled rides (0s duration, lat,lon = 0)

For a production solution, I would probably load this data into an OLAP system such as Amazon Redshift, Google BigQuery, etc to compute aggregations on more massive datasets - would cache aggregations separately in postgreSql. One important note to consider, using these managed services is expensive, there must be some cost-benefit analysis done on whether this is worth the spend - many of these questions are more related to BI rather than as a product feature, so aggregations may be done infrequently



