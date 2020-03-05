import requests
import sys
import os.path


def __print__(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


def fetch(symbol):
    symbol = symbol.upper()
    cookies = {
        'A1': 'd=AQABBEktQV4CEGYugLur4jcJG2zLHezPhskFEgEBAQF-Ql5LXgAAAAAA_SMAAAcISS1BXuzPhsk&S=AQAAAnVd7_Im78AQnSwzD-u3TMk',
        'A3': 'd=AQABBEktQV4CEGYugLur4jcJG2zLHezPhskFEgEBAQF-Ql5LXgAAAAAA_SMAAAcISS1BXuzPhsk&S=AQAAAnVd7_Im78AQnSwzD-u3TMk',
        'B': 'cj1mfthf42ba9&b=3&s=au',
        'GUC': 'AQEBAQFeQn5eS0IgyAR2',
        'A1S': 'd=AQABBEktQV4CEGYugLur4jcJG2zLHezPhskFEgEBAQF-Ql5LXgAAAAAA_SMAAAcISS1BXuzPhsk&S=AQAAAnVd7_Im78AQnSwzD-u3TMk',
        'GUCS': 'AS7BeOFd',
        'PRF': 't%3D'+symbol,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://in.finance.yahoo.com/quote/'+symbol+'/history?p='+symbol,
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }
    params = (
        ('period1', '820454400'),
        ('period2', '1583280000'),
        ('interval', '1d'),
        ('events', 'history'),
        ('crumb', 'hz0Swm5WoOd'),
    )
    __print__("downloading .. "+symbol)
    response = requests.get('https://query1.finance.yahoo.com/v7/finance/download/'+symbol,
                            headers=headers, params=params, cookies=cookies)
    response.raise_for_status()  # ensure we notice bad responses

    file = open("./data/" + symbol + ".csv", "w")
    file.write(response.text)
    file.close()
    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('https://query1.finance.yahoo.com/v7/finance/download/IDEA.NS?period1=820454400&period2=1583280000&interval=1d&events=history&crumb=hz0Swm5WoOd', headers=headers, cookies=cookies)


file = open(sys.argv[1])
lines = file.readlines()
stock_list = list()
for line in lines:
    stock_list.append(line.rstrip()+".NS")
i = len(stock_list)
for symbol in stock_list:
    i -= 1
    print("doing ", i)
    if not os.path.isfile("./data/"+symbol+".csv"):
        fetch(symbol)
    else:
        __print__("already exists for ", symbol)
