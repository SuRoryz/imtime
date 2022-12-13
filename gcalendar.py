from __future__ import print_function
import datetime
import googleapiclient
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

calendarId = 'tkrsue@gmail.com'
SERVICE_ACCOUNT_FILE = 'boilpoint-bb8dfdb6d09a.json'


class GoogleCalendar(object):

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    def create_event_dict(self, name, desc, start_date, end_date):
        event = {
            'summary': name,
            'description': desc,
            'start': {
                'dateTime': start_date,
            },
            'colorId': 8,
            'end': {
                'dateTime': end_date,
            }
        }
        return event

    def create_event(self, event):
        e = self.service.events().insert(calendarId=calendarId,
                                         body=event).execute()
        print('Event created: %s' % (e.get('id')))

    def get_events_list(self, date=False, toValid=False):
        if not(date):
            now = datetime.datetime.utcnow().isoformat() + 'Z'
        else:
            if toValid:
                date = datetime.datetime.fromordinal(date.toordinal())
            now = date.isoformat() + "+03:00"
            print(now)
        
        events_result = self.service.events().list(calendarId=calendarId,
                                                   timeMin=now,
                                                   maxResults=10, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            
        list_events = []
        
        for event in events:
            print(str(date.date()), event['start'].get('dateTime', event['start'].get('date'))[:10])
            if event['start'].get('dateTime', event['start'].get('date'))[:10] != str(date.date()): 
                continue
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            list_events.append([start, end, event['summary']])
        
        return list_events