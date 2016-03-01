#Astroutils
A collection of simple astronomy utilities written mostly in Python.


 * darksky : A python script to generate information to assist planning of observing sessions. Displays moon interference for each day in the calendar year.

----------
**darksky.py**
A python script to generate information to assist planning of observing sessions. Displays moon interference for each day in the calendar year.

Output Legend:
S - Sun is above horizon
M - Moon is above horizon
Moon P - Moon Phase, 0 is New moon 100 is Full moon.

The time line starts at 6 PM and ends at 6 AM next day. Each division is 15 minutes.

This script depends PyEphem http://rhodesmill.org/pyephem/ to do the calculations. Please install this python library before using the script. If you have **pip** installed you can easily install it by running this:

    $ pip install pyephem

 You can run the script with -h switch to list all the options.

    $ python darksky.py -h                                                                                                                               
    usage: darksky.py [-h] [--weekends] [--colorize] [--splitmonths]
                      year latitude longitude minDarkHours
    
    positional arguments:
      year           The year for which you want to run darksky
      latitude       Latitude of observer
      longitude      Longitude of observer. Positive for east and negative for
                     west
      minDarkHours   Minimum number of dark hours. Example 4
    
    optional arguments:
      -h, --help     show this help message and exit
      --weekends     Limit run to weekends
      --colorize     Use colours to indicate weekends
      --splitmonths  Break output to show months 

The output

**Examples**

    python darksky.py --colorize --splitmonths  2016 13.0 80.0 4

List for the year 2016, Location Chennai 80E 13N and minimum dark period of 4 hours. Also colorise weekends and split output by months.


    python darksky.py --colorize --splitmonths --weekends 2016 13.0 80.0 4

List for the year 2016, Location Chennai 80E 13N, weekends only and minimum dark period of 4 hours. Also colorise weekends and split output by months.

