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

    for i in range(len(df)):
        ticket_api.update_ticket(df['index'][i], df['sentiment_mapping'][i])