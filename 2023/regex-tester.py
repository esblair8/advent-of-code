import re

regex_result = re.findall(
    rf'(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))', 'gctcfive3l8twonezbr')
print(regex_result)
print(regex_result[0])
print(regex_result[-1])

print(rf'\d+', 'Game   1')
print(re.findall(rf'\d+', 'Game  10'))
print(re.findall(rf'\d+', 'Game 100'))
