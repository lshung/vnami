from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor


class Helper():
    # Execute thread pool
    @staticmethod
    def execute_thread_pool(tasks, max_workers=10):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(f, *args) for f, args in tasks]
            results = [future.result() for future in futures]
            return results
    
    # Get the last working day, which is not Saturday or Sunday
    @staticmethod
    def get_last_working_day():
        today = datetime.today()
        if today.weekday() == 5: # Today is Sat then minus 1 day
            today -= timedelta(days=1)
        elif today.weekday() == 6: # Today is Sun then minus 2 days
            today -= timedelta(days=2)
        elif today.weekday() == 0 and today.hour < 15: # Today is Mon morning so minus 3 days
            today -= timedelta(days=3)
        else:
            if today.hour < 15: # Before 3 p.m
                today -= timedelta(days=1)
        return today.strftime('%Y/%m/%d')

    
# For testing purposes only
if __name__ == "__main__":
    print(Helper.get_last_working_day())
