import re

line = 'gctcfive3l8twonezbr'

regex_result = re.findall(rf'(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))',line)
print(regex_result)
print(regex_result[0])
print(regex_result[-1])


