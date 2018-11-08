import pandas as pd

# Import sklearn.preprocessing.StandardScaler
from sklearn.preprocessing import MinMaxScaler


def get_normalised_data(data):
    """
    Normalises the data values using MinMaxScaler from sklearn
    :param data: a DataFrame with columns as  ['index','Open','Close','Volume']
    :return: a DataFrame with normalised value for all the columns except index
    """
    # Initialize a scaler, then apply it to the features
    scaler = MinMaxScaler()
    numerical = ['Open Price', 'High Price','Low Price','Close Price', 'Volume']
    dataNormalized = data.copy(deep=True)
    dataNormalized[numerical] = scaler.fit_transform(dataNormalized[numerical])

    return dataNormalized


def remove_data(data):
    """
    Remove columns from the data
    :param data: a record of all the stock prices with columns as  ['Date','Open','High','Low','Close','Volume']
    :return: a DataFrame with columns as  ['index','Open','Close','Volume']
    """
    # Define columns of data to keep from historical stock data
    item = []
    openPrice = []
    highPrice = []
    lowPrice = []
    closePrice = []
    volume = []

    # Loop through the stock data objects backwards and store factors we want to keep
    i_counter = 0
    for i in range(len(data) - 1, -1, -1):
        item.append(i_counter)
        openPrice.append(data['Open Price'][i])
        closePrice.append(data['Close Price'][i])
        highPrice.append(data['High Price'][i])
        lowPrice.append(data['Low Price'][i])
        volume.append(data['Volume'][i])
        i_counter += 1

    # Create a data frame for stock data
    stocks = pd.DataFrame()

    # Add factors to data frame
    stocks['Item'] = item
    stocks['Open Price'] = pd.to_numeric(openPrice)
    stocks['Close Price'] = pd.to_numeric(closePrice)
    stocks['High Price'] = pd.to_numeric(highPrice)
    stocks['Low Price'] = pd.to_numeric(lowPrice)
    stocks['Volume'] = pd.to_numeric(volume)

    # return new formatted data
    return stocks