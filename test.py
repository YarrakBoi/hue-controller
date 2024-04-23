import requests
import urllib3

urllib3.disable_warnings()
light_1_rid = "2cbad179-b90c-4f0d-858b-9cb9a1029372"

url = "https://192.168.1.100/clip/v2/resource/light/" + light_1_rid
param = {"devicetype":"app_name#instance_name", "generateclientkey": True}
app_key = "NDHJIvbYnlf6pdYgUau4k4IAQxz42s-ccEMHHV5t"

headers = {"hue-application-key": app_key}
body = {"on" : {"on" : True}}

response = requests.put(url, verify=False, headers=headers, json=body)


print(response.content)