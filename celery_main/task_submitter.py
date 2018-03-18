from celery_main.task_receiver import get_response
import time

if __name__ == '__main__':
    links = list()
    with open("one_million_websites.txt", "r") as f:
        links = f.readlines()

    start_time = time.time()
    for index, link in enumerate(links):
        link = link.strip()
        result = get_response.delay(link, index)
        print(str(index) + ' task submitted ' + link)
        if index % 1000 == 999:
            break

    print("submitted in "+ str(time.time() - start_time))
