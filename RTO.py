import os
import time
import socket
import csv
import requests

url = input("Enter domain URL (include http:// or https://): ")
domain= input("Please input your business domain/ cateogory in order to process the RTO accordingly. Choose between "
              "health care , telecom ,university , other")
if domain.lower() == "health care":
    rto = 2
    print("Your RTO is : less than " + str(rto) + " hours ")
    print("as standardized by " + "Tech Target Company , A Business impact analysis for business continuity")
    print("for being in the critical Category")
    print("and also  by University of Missouri for System Business Continuity Classification (Jan-12) ")

elif domain.lower() == "telecom":
    rto = 24
    print("Your RTO is : " + str(rto) + " as standardized by ..")
    print("as standardized by " + "Tech Target Company , A Business impact analysis for business continuity")
    print()

elif domain.lower() == "university":
    rto = 4
    print("Your RTO is : less than " + str(rto) + " hours ")
    print("as standardized by " + "Tech Target Company , A Business impact analysis for business continuity")
    print("for being in the critical Category")
    print("and also  by University of Missouri for System Business Continuity Classification (Jan-12) ")

elif domain.lower() == "other":
    rto = float(input("Enter the your recovery time objective which means the amount of time an organization needs to "
                  "bring critical systems back online "))
present = 0 # there is no such a domain name
running_time = 0

ip_address = " "
down_start_time = 0
last_response_time = None
mtd = 0
var = 0
start_time = time.time()
timer = 0
timetoSleep = rto * 60 * 60
def retrieve_domain(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is reachable.")
            return url
        else:
            print(f"{url} returned status code {response.status_code}.")
            return " "
    except requests.exceptions.RequestException as e:
        print(f"{url} is not a valid domain name or is not reachable.")
        return " "
def check_server(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False
def ping_server(url):
    try:
        response = requests.get(url, timeout=5)  # sends an HTTP GET request
        return response.status_code == 200  # checks if the response status is 200 OK
    except requests.exceptions.RequestException:
        return False

def rto_measurement(RTO, ipaddress):
    firstflag=0
    result=0
    while not check_server(url):
        print(url, "is not reachable")
        if firstflag==0:
            time.sleep(RTO)
            firstflag = 1
        else:
            result = 1
            break
    if result == 0:
        print(" YOUR RTO IS SUCCESS ")
    else:
        print(" YOUR RTO IS FAILING ")
""""
    result = 0
    firstflag = 0
    while status == 0:
        response2 = os.system("ping -n 1 " + ipaddress)

        if response2 == 1:
            print(ipaddress, "is not reachable")

            if firstflag == 0:
                time.sleep(RTO)
                firstflag = 1
            else:
                result = 0
                break
        else:
            print('else')
            status = 1
            result = 1

        return result
        """""

try:
    ip_address = socket.gethostbyname(url)
    print(f"IP address of {url}: {ip_address}")
    present = 1 ###there is a domain name with this IP

except socket.gaierror:
    print(f"{url} is not a valid domain name") # variable present will remain 0
    exit()
""" 
while True: #ping ever rto to check if available
    response = os.system("ping -n 1 " + ip_address)
    if response == 1:
        print(ip_address, "is not reachable")
        up = 0 # it is down
        resultofRTO = rto_measurement(up, timetoSleep, ip_address)
        if resultofRTO == 1:
            print(" YOUR RTO IS SUCCESS ")
        else:
            print(" YOUR RTO IS FAILING")
        break

    else :
        print(ip_address, "is reachable")
        print(time.time())
        ####lw haga reachable always what to do
    time.sleep(timetoSleep)
    """
while True:
    if check_server(url):
        print(url, "is reachable")
        print(time.time())
    else:
        print(url, "is not reachable")
        rto_measurement(timetoSleep, url)
        break
    time.sleep(timetoSleep)