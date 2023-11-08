import os
import pandas as pd


class StockPriceCsvModel():
    app_folder = os.path.dirname(os.path.realpath(__file__))
    database_folder = os.path.join(app_folder, 'database')
    
    @classmethod
    def save_stock_data_to_csv(cls, df):
        temp_df = df.copy()
        try:
            symbol = temp_df.iloc[0, 0]
            output_file = os.path.join(cls.database_folder, f'{symbol}.csv')
            temp_df['date'] = temp_df['date'].dt.strftime('%Y/%m/%d') # For Amibroker format
            temp_df.to_csv(output_file, index=False, header=None)
            print(f'Success: {symbol} Saved to CSV file')
        except Exception as e:
            print(f'Error: {symbol} Saved to CSV file. Detail: {e}')
    

# For testing purposes only
if __name__ == "__main__":
    data = {
        'symbol': ['AAPL', 'AAPL', 'AAPL'],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'open': [150.0, 152.0, 154.0],
        'high': [155.0, 157.0, 159.0],
        'low': [149.0, 151.0, 153.0],
        'close': [152.0, 154.0, 156.0],
        'volume': [1000, 1200, 1100]
    }
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    StockPriceCsvModel.save_stock_data_to_csv(df)
    