import re

number_of_request = 0

with open("access_log_Jul95.txt", "r") as file:
    text = file.readlines()

pattern = re.compile('(\\[01/Jul/1995:(((00:0[7-9])|(00:[1-5][0-9])|(01:\\d{2})|(02:[0-2]0)):\\d{2}).*\\]).*(NASA).*')

for line in text:
    match = re.search(pattern, line)
    if match:
        number_of_request += 1

print(number_of_request)
