#!/usr/bin/env python
#- * -coding: utf - 8 - * -

import  ephem
from    datetime import datetime, date, time, timedelta
import  json
import  sys
import  argparse

"""
Script to generate a list of dark sky weekends for a given year.
"""

__author__      = 'Arun Venkataswamy (arun@indstronomy.com)'
__copyright__   = 'Copyright (c) Indstronomy'
__license__     = 'MIT'
__vcs_id__      = '$Id$'
__version__     = '1.0.0' 


def darksky(year,latitude,longitude,minDarkHours,weekends,colorize,splitmonths):

    print 'Year',year,'Lat',latitude,'Long',longitude

    utcx = datetime.now() - datetime.utcnow()
    date1 = datetime(year, 1, 1, 18, 0, 0)
    date2 = datetime(year, 12, 31, 18, 0, 0)
    day = timedelta(days = 1)
    dx = timedelta(seconds = 15 * 60)

    person = ephem.Observer()
    person.lon = str(longitude)
    person.lat = str(latitude)

    sun = ephem.Sun()
    moon = ephem.Moon()

    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    times = ['6P  ','7P  ','8P  ','9P  ','10P ','11P ','12A ','1A  ','2A  ','3A  ','4A  ','5A  ','6A  ']
    table_data = []

    row = ['Date','Day','Moon Phase']
    for a in range(0,12):
        row.append(times[a])
        row.append('')
        row.append('')
        row.append('')

    table_data.append(row)

    while date1 <= date2:

        datex = date1
        row = [date1.strftime('%Y.%m.%d'),days[date1.weekday()]]
        dhours = 0
        for a in range(0,48+3):
            
            dateutc = datex - utcx
            person.date = dateutc

            sun.compute(person)
            moon.compute(person)

            if a == 0:
                row.append(moon.phase)

            if ((sun.alt+0)*180.0/ephem.pi <= -18 and moon.alt < 0):
                row.append(' ')
                dhours = dhours + 0.25
            else:
                if (sun.alt+0)*180.0/ephem.pi < -18:
                    row.append('M')
                else:
                    row.append('S')

            datex = datex + dx

        if dhours >= minDarkHours:
            table_data.append(row)
        date1 = date1 + day


    mnames = ['','January','February','March','April','May','June','July','August','September','October','November','December']

    omonth = '00'
    month = '01'

    for a in range(len(table_data)):
        strx = ''
        if a == 0:
            strx = 'Date       | Day | Moon P | '
            for b in range(3,48):
                strx = strx + table_data[a][b]
            strx = strx + '  |'
            print strx
            strx = '           +     +        + '
            for b in range(3,12+3):
                strx = strx + '|"""'
            strx = strx + '  |'
            print strx
        else :

            if splitmonths:
                omonth = month
                month = table_data[a][0].split('.')[1]
                if omonth != month:
                    omonth = month
                    print '\n'
                    print mnames[int(month)],year
                    print '\n'

            strx = strx + table_data[a][0] + ' | '
            strx = strx + table_data[a][1] + ' | '
            strx = strx + ("%4d" % (int(table_data[a][2]))) + '   | '
            for b in range(3,48+4):
                strx = strx + table_data[a][b]
            strx = strx + ' |'

            if weekends:
                if table_data[a][1] == 'FRI' or table_data[a][1] == 'SAT':
                    if colorize:
                        strx = '\033[91m'+strx+'\033[0m'
                    if int(table_data[a][2]) < 50:    
                        print strx
            else:
                if colorize:
                    if table_data[a][1] == 'FRI' or table_data[a][1] == 'SAT':                    
                        strx = '\033[91m'+strx+'\033[0m'
                print strx

    pass

if __name__=='__main__':
    
    parser = argparse.ArgumentParser()    
    parser.add_argument('--weekends', help="Limit run to weekends", action="store_true")
    parser.add_argument('--colorize', help="Use colours to indicate weekends", action="store_true")
    parser.add_argument('--splitmonths', help="Break output to show months", action="store_true")
    parser.add_argument('year', help='The year for which you want to run darksky', type=int)
    parser.add_argument('latitude', help='Latitude of observer', type=float)
    parser.add_argument('longitude', help='Longitude of observer. Positive for east and negative for west', type=float)    
    parser.add_argument('minDarkHours', help='Minimum number of dark hours. Example 4', type=int)    
    args = parser.parse_args()
    darksky(args.year,args.latitude,args.longitude,args.minDarkHours,args.weekends,args.colorize,args.splitmonths)




