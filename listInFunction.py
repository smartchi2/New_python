import random

list_num = []


def number():
    for index in range(0, 10):
        num = random.randint(1, 51)
        list_num.append(num)
        return list_num


#     print(list_num)


# number()


def getNumber_length(nums):
    count = 0
    for index in nums:
        count += 1
    return count


nums = [12, 3, 90, 15, 10, 11]
digit = getNumber_length(nums)


# print(digit)


def getEvenNumber(number):
    sum = 0
    for index in range(15):
        if index % 2 == 0:
            sum = sum + index
    return sum


# print(getEvenNumber(number))


def getOddNumber(number):
    sum = 0
    for index in range(10):
        if index % 2 != 0:
            sum = sum + index
    return sum


# print(getOddNumber(number))


input = [12, 24, 56, 10, 20, 4]


def multiply(input):
    for index in range(3, len(input), 2):
        input[index] *= 3
        return input


# print(multiply(input))

my_input = [20, 11, 45]


def AverageNumbers(get_ave):
    return sum(get_ave) / len(get_ave)



average = AverageNumbers(my_input)
# print(average)

max = [220, 1, 70, 20, 11]
lagest = max[0]


def max_Number(max):
    for i in max:
        if i > lagest:
            lagest = i
            return lagest


# print(lagest)

min = [10, 50, 70, 100]
smallest = min[0]


def get_smallest_number(min):
    for i in max:
        if i < smalles:
            smallest = i
            return smallest


# print(smallest)


# def get_length_of_string(name):
#     first_name = name[0]
#     second_name = name[len(name) - 1]
#     if first_name == second_name and len(name) >= 2:
#         return name
#     else:
#         return
#
#
# word = "smarts"
# print(get_length_of_string(word))


def check_if_name_is_two(name):
    first_name = name[0]
    second_name = name[len(name) - 1]
    if first_name == second_name and len(name) >= 2:
        return name


word = "DAD"


# print(check_if_name_is_two(word))

def check_duplicate():
    get_duplicate = ["4", "5", "4", "6", "5", "1", "9"]
    get_duplicate = list(dict.fromkeys(get_duplicate))

    return get_duplicate


# print(check_duplicate())

def get_range():
    nums_list = []
    for index in range(1, 15):
        nums_list.append(index)
    return nums_list


# print(get_range())

def number_to_be_pop(duplicate):
    final_inList = []
    for num in duplicate:
        if num not in final_inList:
            final_inList.append(num)
    return final_inList


duplicate = [2, 12, 5, 12, 28, 7, 7, 90, 2, 12]
# print(number_to_be_pop(duplicate))
