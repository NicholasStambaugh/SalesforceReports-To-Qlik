import salesforce_connector
import qlik_sense_connector

def main():
    #connections
    salesforce_conn = salesforce_connector.connect()
    salesforce_data = salesforce_connector.extract_data(salesforce_conn)
    transformed_data = salesforce_connector.transform_data(salesforce_data)
    qlik_sense_conn = qlik_sense_connector.connect()
    qlik_sense_connector.load_data(qlik_sense_conn, transformed_data)
    salesforce_connector.close_connection(salesforce_conn)
    qlik_sense_connector.close_connection(qlik_sense_conn)

if __name__ == "__main__":
    main()
