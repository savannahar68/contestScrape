'''
This is a test file for saving events to google calander
'''
from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '+05:30'      # PDT/MST/GMT-7
EVENT = {
    'summary': 'Test for saving to cals',
    'start':  {'dateTime': '2017-12-28T09:00:00%s' % GMT_OFF},
    'end':    {'dateTime': '2017-12-28T10:00:00%s' % GMT_OFF},
  
}

e = GCAL.events().insert(calendarId='primary',
        sendNotifications=True, body=EVENT).execute()

print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))

'''
datetime_object = datetime.strptime('10:30:00 28-12-2017', '%H:%M:%S %d-%m-%Y')
datetime_object.strftime("%Y-%m-%dT%H:%M:00")

'''
