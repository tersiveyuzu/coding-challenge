import requests
import pandas as pd
from ticket import TicketAPI


def read_data():

    url = "https://datasets-server.huggingface.co/first-rows?dataset=milesbutler%2Fconsumer_complaints&config=milesbutler--consumer_complaints&split=train"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def transform_data(data):

    df = pd.DataFrame.from_dict(data.json(), orient='index')[0]["rows"][:50]
    df = pd.DataFrame(df)['row']

    complaint = []
    issue = []

    for i in range(len(df)):
        complaint.append(df[i]['Consumer Complaint'])
        issue.append(df[i]['Issue'])
        data = pd.DataFrame([complaint, issue]).T
        data.columns = ['body', 'subject']

    data = data.reset_index()
    data['body'] = data['body'] + ' - ' + data['index'].astype(str)
    data['subject'] = data['subject'] + ' - ' + data['index'].astype(str)

    return data


def create_tickets(df):

    ticket_api = TicketAPI()

    for i in range(len(df)):
        ticket_api.create_ticket_with_article(df['index'][i], df['subject'][i], df['body'][i])