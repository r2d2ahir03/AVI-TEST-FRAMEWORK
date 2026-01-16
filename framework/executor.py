from concurrent.futures import ThreadPoolExecutor

def run_parallel(tasks):
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(lambda t: t(), tasks)
