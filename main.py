import os
import json
from keyword import iskeyword
from getLatest import getLatest
from getMany import getMany

if __name__ == '__main__':
    urls = json.load(open('urls.json', 'r'))    
    
    quit = 'n'

    while quit.lower() != 'y':
        keys = []
        i = 0
        for key in urls:
            print(str(i) + ": " + key)
            keys.append(key)
            i += 1
    
        chart = ""
        while not(chart.isdigit() and int(chart) >= 0 and int(chart) < len(urls)):
            chart = input("Choose the chart to download: ")    
    
        chart = int(chart)
        key = keys[chart]

        print("0: download latest\n1: download many")
        mode = ""
        while not(mode.isdigit() and (int(mode) == 0 or int(mode) == 1)):
            mode = input("Choose the dowload mode: ")

        mode = int(mode)

        if not os.path.isdir(key):
            os.mkdir(key)

        if mode == 0:        
            getLatest(key, urls[key])
        else:
            getMany(key, urls[key])

        quit = input("Quit? (y/n): ")


