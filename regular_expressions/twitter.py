import re

url=input("URL: ").strip()
# first method
'''
username=re.sub(r"^(https?://)?(www\.)?x.com/", "", url)
print(f"Username: {username}")
'''
#second method
if matches:=re.search(r"^https:?//(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
