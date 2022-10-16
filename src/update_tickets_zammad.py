from pysentimiento import create_analyzer
import pandas as pd
from ticket import TicketAPI


def predict_tickets(df):

    analyzer = create_analyzer(task="sentiment", lang="en")

    sentiment_predictions = analyzer.predict(df['body'])

    list_0 = []

    for i in range(len(sentiment_predictions)):
        list_0.append(sentiment_predictions[i].output)

    df_predictions = pd.DataFrame(list_0)

    df_enriched = pd.concat([df, df_predictions], axis=1)
    df_enriched.columns = ['index', 'complains', 'issue', 'sentiment']

    sentiment_dict = {'POS': 1, 'NEU': 2, 'NEG': 3}

    df_enriched['sentiment_mapping'] = df_enriched['sentiment'].map(sentiment_dict)
    return df_enriched


def update_tickets(df):

    ticket_api = TicketAPI()

    for i in range(len(df)):
        ticket_api.update_ticket(df['index'][i], df['sentiment_mapping'][i])