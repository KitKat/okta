#!/usr/bin/env python3

################################################################################
# Name	        : User Creator
# Description	: Create Users with a password and default groups
# Author       	: Alex "KitKat" Kikot
# Email         : git@kikot.me
################################################################################

import http.client
import json
import sys

import constants

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

################################################################################

authorization = "SSWS " + constants.authorization
conn = constants.conn + "-admin.okta.com"
cookie = "JSESSIONID=" + constants.cookie 
domain_name = "domain.com"

with open("user_list.json", "r") as json_file:
    user_list = json.load(json_file)

conn = http.client.HTTPSConnection(conn)

# Default Groups
default_groups = [""]

for user in user_list:
    first_name = user["first_name"]
    last_name = user["last_name"]
    user_password = user["user_password"]
    user_groups = user["custom_groups"]
    domain_email = f"{first_name.lower()}.{last_name.lower()}@{domain_name}"

    payload = json.dumps(
        {
            "profile": {
                "firstName": first_name,
                "lastName": last_name,
                "email": domain_email,
                "login": domain_email,
            },
            "credentials": {"password": {"value": user_password}},
            "groupIds": default_groups + user_groups,
        }
    )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": authorization,
        "Cookie": cookie,
    }

    conn.request("POST", "/api/v1/users", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))