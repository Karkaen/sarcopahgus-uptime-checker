import json
import requests
import numpy as np


def uptimeCheck(address) :
    url = "https://api.encryptafile.com/arch-uptime-statistics"
    response = requests.get(url)
    return response.json()[address]["uptimeRatio"]

while True : 
    myAddress = input("Enter your wallet address : ")
    try :    
        if len(myAddress) == 42 :
            result = uptimeCheck(myAddress)
            print(f"Your uptime is {result}")
            sorted_data = requests.get("https://api.encryptafile.com/arch-uptime-statistics").json()
            sorted_addresses = sorted(sorted_data, key=lambda x: sorted_data[x]["uptimeRatio"], reverse=True)
            my_rank = sorted_addresses.index(myAddress) + 1
            print(f"Your rank is {my_rank} out of {np.argmax(sorted_addresses)} addresses")
            break     
        else :
            print("Wrong wallet address.Please check it before trying again")
    except :
        print("not exist")

# 0x7c2dC9d2f6C9Ba7581fADa1fe6d0BBf0317c5208