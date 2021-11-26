#!/usr/bin/env python
# coding: utf-8

from time import time

start = time()

import os

path = os.getcwd()

def read_txt(file):
    with open(file,'r') as f:
        content = f.readlines()
    return content

adm_id = read_txt(f'{path}\\adm_id.txt')[0].strip()

adm_pass = read_txt(f'{path}\\adm_password.txt')[0].strip()

ids = read_txt(f'{path}\\list_of_ids.txt')

user_list = [i.strip('\n') for i in ids]


from pyad import aduser

from pyad import *

# our username and password 
pyad.set_defaults(username= adm_id , password = adm_pass)

from time import sleep

count = 1

for username in user_list:
    try:
        user = aduser.ADUser.from_cn(username)
        sleep(1)
        status = user.disable()
        sleep(0.5)
        if status == None:
            print(f'{count}. {username} disabled')
        if count == len(user_list):
            print("*************Job Finished**************")
    except:
        print(f' error  at {username}')
        

print(f'All done in {round((time()-start),0)} Seconds')
