# solar-wind-music (WIP)
This is a Pure Data patch that generates music from solar wind data, which is gathered & processed with Python (scripts in /py).  
The processed data is sent to Pd via `tcp` & `netreceive`.  
Data source: https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json

## Prerequisites
Pure Data Vanilla  
freeverb~ (Pd external library)

## Usage
run `solar-wind-music.pd`  

## Todo
1. real time data processing
2. integerating hardware sensors (humidity, temperature, etc.)
3. cleaning up the messy interface... 
