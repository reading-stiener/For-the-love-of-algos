import math
def isPrime(n):
    # Write your code here
    sqrt = math.ceil(math.sqrt(n))
    for i in range(2, sqrt+1):
        if n % i == 0:
            return i
    return 1

def digit_sum(n):
    total = 0
    while n > 0: 
        total += n % 10
        n //= 10
    return total

def lotteryCoupons(n):
    # Write your code here
    s_dict = {}
    most_wins = 1
    for i in range(1, n+1):
        tot = digit_sum(i)
        if s_dict.get(tot, -1) == -1:
            s_dict[tot] = 1
        else:
            s_dict[tot] += 1
            most_wins = max(s_dict[tot], most_wins)
    most_win_count = 0
    for s, winners in s_dict.items():
        if winners == most_wins:
            most_win_count += 1
    return most_win_count

def getShiftedString(s, leftShifts, rightShifts):
    # Write your code here
    n = len(s)
    list_str = list(s)
    print(list_str)
    for i in range(n):
        idx = (i - leftShifts) % n 
        list_str[idx] = s[i]
    s = "".join(list_str)
    list_str = list(s)
    for i in range(n):
        idx = (i + rightShifts) % n
        list_str[idx] = s[i]
    s =  "".join(list_str)
    return s 

def degreeOfArray(arr):
    # Write your code here
    deg_dict = {}
    n = len(arr)
    deg = 1
    sub_arr_len = 1 
    for i in range(n):
        if deg_dict.get(arr[i], -1) == -1:
            deg_dict[arr[i]] = (1, [i])
        else:
            count = deg_dict[arr[i]][0] + 1
            arr_idx = deg_dict[arr[i]][1][:]
            arr_idx.append(i)
            if count > deg:
                deg = count
                sub_arr_len = arr_idx[-1] - arr_idx[0] + 1 
            elif count == deg and arr_idx[-1] - arr_idx[0] + 1 < sub_arr_len:
                deg = count
                sub_arr_len = arr_idx[-1] - arr_idx[0] + 1 
            deg_dict[arr[i]] = (count, arr_idx)
    return sub_arr_len


def palindrome(s):
    # Write your code here
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(n-i):
            if s[j:j+i+1] not in substrings:
                substrings.append(s[j:j+i+1])

    count = 0
    for string in substrings:
        if isPalindrome(string):
            print(string)
            count += 1
    return count

import requests
from pprint import pprint
import requests
from pprint import pprint
def avgRotorSpeed(statusQuery, parentId):
    # Write your code here
    endpoint = "https://jsonmock.hackerrank.com/api/iot_devices/search" 
    params ={
        "status": statusQuery
    }
    response = requests.get(url=endpoint, params=params) 
    raw = response.json()  
    pages = raw["total_pages"]
    total_rotor_speed = 0
    count = 0
    for i in range(1, pages+1):
        params["page"] = i
        r  =  requests.get(url=endpoint, params=params)
        data = r.json()
        data_arr = data["data"]
        pprint(data_arr)
        total_rotor_speed = 0
        count = 0
        for data_pts in data_arr:
            if data_pts.get("parent", -1) != -1:
                if data_pts["parent"] != None and data_pts["parent"]["id"] == parentId:
                    total_rotor_speed += data_pts["operatingParams"]["rotorSpeed"]
                    count += 1
    return math.floor(total_rotor_speed / count)
if __name__ == "__main__":
    print(degreeOfArray([1,1,2,1,2,2]))
    print(avgRotorSpeed("RUNNING", 7))