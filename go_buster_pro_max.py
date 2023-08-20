import requests as req
import sys
import time

if len(sys.argv) == 3:
    # ip = "172.105.72.232"
    ip = sys.argv[1]
    port = 80
    fileName = sys.argv[2]

    baseUrl = f"http://{ip}:{port}"
    dirs = set()

    try:
        with open("wordlist.txt", 'r') as wordlist:
            for word in wordlist:
                testingUrl = baseUrl + "/" + word
                res = req.get(testingUrl)
                if 200 <= res.status_code < 300:
                    dirs.add(word)
                time.sleep(0.2)
    except Exception as e:
        print(e)

    if len(dirs) != 0:
        print("Found the following directories...")
        for directory in dirs:
            print(directory)
else:
    print("Invalid number of arguments!")
