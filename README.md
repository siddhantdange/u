
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

### Dependencies
You will need python 2.7 to run these scripts and `pip` to install the dependencies

#### Install
```
source env/bin/activate
pip install -r requirements.txt
```

## Usage
Run `./generate_small_medium_data_samples.sh # generates data samples, assumes downloaded data is in proper location as per 'Setup'`
Run `./run_analytics.sh`

*Be sure to use this script as the entrypoint to running the application*

