def read_file(file_name):
    file_obj = open(file_name, "r")  # opens the file in read mode
    words = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return words


def count_increases(arr, window):
    count = 0
    last = 0
    for i in range(len(arr) - window):
        window_sum = 0
        for j in range(window):
            window_sum += int(arr[i + j])
        if last < window_sum:
            count += 1
        last = window_sum
    return count


array = read_file("input01.txt")
print("Count of increase times is ", count_increases(array, 1))
print("Count of increase in 3 number window", count_increases(array, 3))
