def get_multiplied_digits(number):
    str_numbers = str(number)
    first_number = int(str_numbers[0])
    if len(str_numbers) > 1:
        return first_number * get_multiplied_digits(int(str_numbers[1:]))
    else:
        return first_number


result = get_multiplied_digits(40203)
print(result)
