COTWO_INDICATOR = "cotwo"
OXYGEN_INDICATOR = "oxygen"


# Part One
def power_diagnostic(data):
    bucket = [0] * len(str(data[0]))
    for element in data:
        for idx in range(len(element)):
            bucket[idx] = bucket[idx] + 1 if element[idx] == '1' else bucket[idx] - 1
    epsilon = ''
    gamma = ''
    for element in bucket:
        epsilon = epsilon + '0' if element < 0 else epsilon + '1'
        gamma = gamma + '1' if element < 0 else gamma + '0'
    print("Power_Diagnostics: Epsilon: ", epsilon, ", Gamma: ", gamma, ", Result: ", int(epsilon, 2) * int(gamma, 2))


# Part Two
def support_diagnostic(bucket):
    oxygen = support_diagnostic_by_type(OXYGEN_INDICATOR, bucket, 0)
    ctwo = support_diagnostic_by_type(COTWO_INDICATOR, bucket, 0)
    print("Oxygen / CO2 diagnostic: Oxygen: ", oxygen, ", CO2: ", ctwo, ", Support: ", int(oxygen, 2) * int(ctwo, 2))


def support_diagnostic_by_type(diagnosis_type, bucket, idx):
    if len(bucket) == 1 or idx == len(bucket[0]):
        return bucket[0]
    value_to_compare = get_most_or_less_common_use_bit_in_index(bucket, idx, diagnosis_type)
    bucket = [element for element in bucket if int(element[idx]) == value_to_compare]
    return support_diagnostic_by_type(diagnosis_type, bucket, idx + 1)


def get_most_or_less_common_use_bit_in_index(bucket, idx, diagnosis_type):
    count = 0
    for element in bucket:
        count = count + 1 if element[idx] == '1' else count - 1
    most_common = 1 if count >= 0 else 0
    return most_common if diagnosis_type == OXYGEN_INDICATOR else most_common ^ 1


list_bytes = open("input03.txt").read().splitlines()
power_diagnostic(list_bytes)
support_diagnostic(list_bytes)
