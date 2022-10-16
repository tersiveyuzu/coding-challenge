from import_tickets_zammad import read_data, transform_data, create_tickets
from update_tickets_zammad import predict_tickets, update_tickets
import logging


if __name__ == "__main__":

    logging.info('-1- READ DATA')
    raw_df = read_data()
    logging.info('-2- TRANSFORM DATA')
    enriched_df = transform_data(raw_df)
    logging.info('-3- CREATE TICKETS')
    create_tickets(enriched_df)
    logging.info('-4- PREDICT SENTIMENTS SCORES OF TICKETS')
    df_with_sentiment_scores = predict_tickets(enriched_df)
    logging.info('-5- UPDATE PRIORITIES OF TICKETS')
    update_tickets(df_with_sentiment_scores)