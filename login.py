#!/usr/bin/env python3
# CGI LAB code from Demo 

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import secret
from http.cookies import SimpleCookie


s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password

print("Content-Type: text/html")

#Cookies
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None

# Get and user data if stored in a cookie
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password")

# Credentials Match
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# If cookie is fine, then set it up
if cookie_ok:
    username = cookie_username
    password = cookie_password

if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}\n")

if not username and not password:
    print(login_page())
elif username==secret.username and password==secret.username:
    print(secret_page(username, password))
else:
    print(login_page())
    print("username password: ", username, password) 