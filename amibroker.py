import os
from helper import Helper
import win32com.client


class AmiBroker():
    app_folder = os.path.dirname(os.path.realpath(__file__))
    database_folder = os.path.join(app_folder, 'database')
    format_file_path = os.path.join(app_folder, 'vnami.format')

    # Import data into Amibroker and refresh
    @classmethod
    def import_data(cls, symbol):
        if Helper.is_amibroker_opened():
            try:
                amibroker = win32com.client.Dispatch("Broker.Application")
                data_file_path = os.path.join(cls.database_folder, f"{symbol}.csv")
                amibroker.Import(0, data_file_path, cls.format_file_path)
                amibroker.RefreshAll()
            except Exception as e:
                print(e)


# For testing purposes only
if __name__ == "__main__":
    AmiBroker.import_data("HPG")
    