# SQL Injection - Bypassing login functionallity
 This lab contains a SQL injection vulnerability in the login function.

## Challenge
To solve the lab, perform a SQL injection attack that logs in to the application as the administrator user. 

## Target:
Log into as the administrator using SQL Injection

## QUERY:
''' bash
SELECT * FROM users WHERE username='administrator'-- AND password='whateverpassword'
'''

In this instance, the payload is administrator'--
