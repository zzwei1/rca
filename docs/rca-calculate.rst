Calculate RCA values
--------------------

RCA is a measure of the difference between a given day's median 95th percentile clutter area reflectivity and previously determined baseline 95th percentile clutter area reflectivity.

To calculate RCA, several key pieces are required: a full day or radar files, a clutter map, and a baseline value. All of these are input in the daily_rca routine. The .json configuration file should be edited appropriately to specify the correct paths and dates. 

.. code-block:: python

   # import commands
   from .daily_rca import daily_rca

   # select date, radar band and scan type and find corresponding configuration file
   # edit radar configuration file appropriately
   radar_config_file = '/__your_path_to__/rca/src/rca/config/__band_scan.json__'
   date = 'YYYYMMDD'
   daily_rca(radar_config_file,date)

   # to calculate daily RCA for multiple days (i.e. one week), loop the daily_rca function
   week = ['01','02','03','04','05','06','07']
   for day in week:
       date = '201910'+day
       daily_rca(radar_config_file,date)


