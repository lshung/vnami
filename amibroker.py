import os
from helper import Helper
import win32com.client


class AmiBroker():
    app_folder = os.path.dirname(os.path.realpath(__file__))
    database_folder = os.path.join(app_folder, 'database')
    format_file_path = os.path.join(app_folder, 'vnami.format')
    amibroker = None

    # Get Amibroker instance
    @classmethod
    def get_amibroker_instance(cls):
        if cls.amibroker is None and Helper.is_amibroker_opened():
            cls.amibroker = win32com.client.Dispatch("Broker.Application")
        return cls.amibroker
    
    # Import data of symbols in the database into Amibroker
    @classmethod
    def import_data(cls, symbols=[]):
        if len(symbols) == 0:
            symbols = [os.path.splitext(file)[0] for file in os.listdir(cls.database_folder)] # Symbols that exist in the database
        
        amibroker = cls.get_amibroker_instance()
        if amibroker is not None:
            for symbol in symbols:
                try:
                    data_file_path = os.path.join(cls.database_folder, f"{symbol}.csv")
                    amibroker.Import(0, data_file_path, cls.format_file_path)
                    amibroker.RefreshAll()
                    print(f"Success: Import data of {symbol} into Amibroker")
                except Exception as e:
                    print(f"Error: Cannot import data of {symbol} into Amibroker. Detail: {e}")


# For testing purposes only
if __name__ == "__main__":
    AmiBroker.import_data()
    