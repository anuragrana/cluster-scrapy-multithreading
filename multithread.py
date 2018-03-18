from multiprocessing.dummy import Pool as ThreadPool
import time
import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}

status_timeouts = 0
status_success = 0
status_others = 0
status_exception = 0


def get_all_links():
    links = list()
    with open("one_thousand_websites.txt", "r") as f:
        links = f.readlines()

    links = [link.strip() for link in links]
    return links


def get_response(url):
    print('URL received ' + url)
    response = None
    try:
        response = requests.get(url, headers=headers, timeout=3)
    except requests.exceptions.Timeout as e:
        global status_timeouts
        status_timeouts += 1
    except Exception as e:
        global status_exception
        status_exception += 1

    if response:
        print("-- STATUS --" + str(response.status_code))

        if response.status_code == 200:
            global status_success
            status_success += 1
        else:
            global status_others
            status_others += 1



def multi_thread():
    start_time = time.time()

    # make the Pool of workers
    pool = ThreadPool(180)

    # read the handles.txt file for instagram handles
    links = get_all_links()

    # call the start function in different thread for each handle
    pool.map(get_response, links)
    # print(results)

    # close the pool and wait for the work to finish
    pool.close()
    pool.join()

    print("Finished in  ", time.time() - start_time, " seconds")
    print("success " + str(status_success))
    print("timeout " + str(status_timeouts))
    print("exception " + str(status_exception))
    print("others " + str(status_others))

multi_thread()


