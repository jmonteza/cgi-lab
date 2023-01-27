#!/usr/bin/env python3

import os
import json
# print("Content-Type: text/html")
print("Content-Type: application/json")
print()
# print(os.environ)

print(json.dumps(dict(os.environ), indent=2))

# print(f"<p>HTTP_USER_AGENT= {os.environ['HTTP_USER_AGENT']}</p>")

# 3) HTTP_USER_AGENT

# 4) cgi.FieldStorage()
# s.getfirst()
# s.getfirst()

# 5) Set-Cookie

# 6) HTTP_COOKIE
# cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
# cookie.get("username")
# cookie.get("password")

# 7) javascript:document.cookie= "username=archit"
# javascript:document.cookie = "password=secure"
# data

# 8) hello.py login.py secret.py
