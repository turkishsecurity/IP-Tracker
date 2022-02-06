import requests
import json


banner = """
IP Tracer
Coded by Xale ~ @xaletr
"""

target = input("Target Address => ")

r = requests.get("http://ip-api.com/json/"+target)

j = json.loads(r.text)

if j['status'] in 'success':
 print("[!] Informations Found")
 print("Country : "+j["country"])
 print("Country Code : "+j["countryCode"])
 print("Region : "+j["region"])
 print("Region Name : "+j["regionName"])
 print("City : "+j["city"])
 print("ISP : "+j["isp"])
 print("Query : "+j["query"])
else:
 print("[!] Error Created")
