calibration_values = []

def get_calibrated_value(str):
    return if (len(str) == 0) 0 else str[0] + str[-1]

with open("test.txt", "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        digits = ''
        for i in line:
            if (i.isdigit()):
                digits += i
        calibration_values.append(get_calibrated_value(digits))

print(sum(map(int, calibration_values)))
