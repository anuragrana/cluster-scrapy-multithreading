from celery_main.celery import app
import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}


@app.task
def get_response(url, index):
    print('URL received ' + url)
    response = None
    try:
        response = requests.get(url, headers=headers, timeout=3)
    except requests.exceptions.Timeout as e:
        log_count("status_timeouts")
    except Exception as e:
        pass

    if response:
        print("-- STATUS -- " + str(index) + "--" + str(response.status_code))

        if response.status_code == 200:
            log_count("status_success")
        else:
            log_count("status_others")


def log_count(response_type):
    with open(response_type + ".txt", "r+") as f:
        count = int(f.read())
        f.seek(0)
        f.write(str(count + 1))
