from helper import Helper
from stock_price import StockPrice
from company_info import CompanyInfo
from csv_model import StockPriceCsvModel


class StockPriceScraper():
    @staticmethod
    def scrape():
        symbol_list = CompanyInfo.get_stock_list_from_ssi()['symbol'].to_list()
        print(f'Total number of symbols: {len(symbol_list)}')
        symbol_list = StockPriceCsvModel.get_stocks_to_be_scraped(symbol_list)
        print(f'The number of symbols that need to be scraped: {len(symbol_list)}')
        
        # Scrape data
        tasks = [(StockPrice.get_ohlcv_data, (symbol, )) for symbol in symbol_list]
        result = Helper.execute_thread_pool(tasks)
        result = [x for x in result if x is not None] # Remove items that are None
        
        # Save data to CSV files
        for df in result:
            StockPriceCsvModel.save_stock_data_to_csv(df)


# For testing purposes only
if __name__ == "__main__":
    StockPriceScraper.scrape()
    