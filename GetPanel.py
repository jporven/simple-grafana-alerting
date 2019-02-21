import pycurl
import os
import time
import datetime
from StringIO import StringIO
import sys

grafanaToken = os.getenv("GRAFANA_TOKEN",'none')
grafanaURL = os.getenv("GRAFANA_URL",'none')

def setURL(value):
  '''Grafana shared link as "Direct link rendered image" url modified to change time range.'''
  grafanaURL = 'http://localhost:3000/render/d-solo/6ChrAnrmz/test-dashboard?orgId=1&panelId=2&from=now-1h&to=now&width=1000&height=500&tz=UTC-05%3A00'
  return grafanaURL

def GetGrafanaImage():
  '''
  Get grafana image from static link an save to /tmp directory
  '''
  try:
    buffer = StringIO()
    with open('/tmp/grafchart.png', 'wb') as f:
      c = pycurl.Curl()
      c.setopt(c.URL, setURL(value))
      #Changeit
      c.setopt(c.HTTPHEADER, ['Authorization: Bearer eyJrIjoiMW05RVVwRXFsZ1hncHVsSm04NWE3VXdPalVxxxxx'])
      c.setopt(c.WRITEDATA, f)
      c.perform()
      c.close()
    return 0
  except:
      return -1
#Print URL and error code for testing purposes
#print(setURL(1))
print(GetGrafanaImage())
