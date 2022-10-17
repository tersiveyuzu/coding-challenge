from pysentimiento import create_analyzer
import pandas as pd
import constants
from ticket import TicketAPI


def predict_tickets(df):

    analyzer = create_analyzer(task="sentiment", lang="en")

    sentiment_predictions = analyzer.predict(df['body'])

    empty_list = []

    for i in range(len(sentiment_predictions)):
        empty_list.append(sentiment_predictions[i].output)

    df_predictions = pd.DataFrame(empty_list)

    df_enriched = pd.concat([df, df_predictions], axis=1)
    df_enriched.columns = ['index', 'complains', 'issue', 'sentiment']

    df_enriched['sentiment_mapping'] = df_enriched['sentiment'].map(constants.sentiment_dict)
    return df_enriched


def update_tickets(df):

    ticket_api = TicketAPI()
    list_tickets = ticket_api.list_tickets()
    index_diff = list_tickets[-1]['id'] - len(df) + 1

    for i in range(list_tickets[0]['id'], list_tickets[-1]['id']):
        ticket_api.update_ticket(i, df['sentiment_mapping'][i - index_diff])