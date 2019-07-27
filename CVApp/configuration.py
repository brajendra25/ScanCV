"""
Configurations file
"""
import re
import os

# Get environment variable or return default value
def get_env_var(var, default):
    try:
        env_var = os.environ[var]
        return env_var
    except:
        return default

def isfile(path):
    return os.path.isfile(path)

# Regular expressinos used
bullet = r"\(cid:\d{0,2}\)"
email = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
def get_phone(i,j,n):
    return r"\(?(\+)?(\d{1,3})?\)?[\s-]{0,1}?(\d{"+str(i)+"})[\s\.-]{0,1}(\d{"+str(j)+"})[\s\.-]{0,1}(\d{"+str(n-i-j)+"})"
not_alpha_numeric = r'[^a-zA-Z\d]'
number = r'\d+'
