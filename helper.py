from concurrent.futures import ThreadPoolExecutor


class Helper():
    # Execute thread pool
    @staticmethod
    def execute_thread_pool(tasks, max_workers=10):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(f, *args) for f, args in tasks]
            results = [future.result() for future in futures]
            return results

    
# For testing purposes only
if __name__ == "__main__":
    pass
