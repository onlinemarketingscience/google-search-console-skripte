#
#
# web: https://onlinemarketingscience.com
# twitter: @MarvinJoers
# author: Marvin Jörs
# date: 2017-11-25
#
#          

import argparse
import sys
import statistics
import datetime
from googleapiclient import sample_tools

# Eingabefelder für URL, Start- und Enddatum 
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('property_uri', type=str,
                       help=('Site or app URI to query data for (including '
                             'trailing slash).'))
argparser.add_argument('start_date', type=str,
                       help=('Start date of the requested date range in '
                             'YYYY-MM-DD format.'))
argparser.add_argument('end_date', type=str,
                       help=('End date of the requested date range in '
                             'YYYY-MM-DD format.'))

# Die Main-Funktion
def main(argv):
  service, flags = sample_tools.init(
      argv, 'webmasters', 'v3', __doc__, __file__, parents=[argparser],
      scope='https://www.googleapis.com/auth/webmasters.readonly')    
  
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['date']
  }
  response = execute_request(service, flags.property_uri, request)
  parse_output(response)  

# Funktion: Anfrage an GSC senden
def execute_request(service, property_uri, request):

  return service.searchanalytics().query(
      siteUrl=property_uri, body=request).execute()
   

# Datei schreiben 
f = open('stats-' + datetime.datetime.today().strftime('%Y-%m-%d') + '.csv','w')
f.write('arithmetisches mittel, harmonisches mittel, median, median (low), median (high), standard-abw., varianz, stichprobenabw., stichprobenvarianz \n')

# Parsen des Outputs
def parse_output(response):

  # Deklarieren der Arrays
  clicks =      []
  impressions = []
  ctr =         []
  position =    []   

  if 'rows' not in response:
    print('Google Search Console kann diese Abfrage nicht beantworten.')
    return

  rows = response['rows']

  # jede Zeile speichern wir uns in einem Zahlenarray 
  for row in rows:
    keys = ''
    # keys = date
    if 'keys' in row:
        clicks.append(row['clicks'])
        impressions.append(row['impressions'])
        ctr.append(row['ctr'])
        position.append(row['position'])

  quick_math(clicks)
  quick_math(impressions)
  quick_math(ctr)
  quick_math(position)


def quick_math(array):

  array_stats = []
  map(float, array)

  mean = statistics.mean(array)
  array_stats.append(mean)

  h_mean = statistics.harmonic_mean(array)
  array_stats.append(h_mean)

  median = statistics.median(array)
  array_stats.append(median)

  median_low = statistics.median_low(array)
  array_stats.append(median_low)

  median_high = statistics.median_high(array)
  array_stats.append(median_high)

  # noch buggy
  #mode = statistics.mode(array)
  #array_stats.append(mode)

  pstdev = statistics.pstdev(array)	
  array_stats.append(pstdev)

  pvariance = statistics.pvariance(array)
  array_stats.append(pvariance)

  stdev = statistics.stdev(array)
  array_stats.append(stdev)

  variance = statistics.variance(array)
  array_stats.append(variance)
 
  f.write('"""' + str(mean).replace(".",",") + '"","' + str(h_mean).replace(".",",") + '","' + str(median).replace(".",",") + '","' + str(median_low).replace(".",",") + '","' + str(median_high).replace(".",",") + '","' + 
  str(pstdev).replace(".",",") + '","' + str(pvariance).replace(".",",") + '","' + str(stdev).replace(".",",") + '","' + str(variance).replace(".",",") + '"\n')


# If-Abfrage zur Ausführung des Skripts
if __name__ == '__main__':
  main(sys.argv)
  f.close()   
