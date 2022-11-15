import validators
lst_of_strings = []
lst_of_valid_url = []
number_of_strings = int(input("input number of strings: "))

for _ in range(number_of_strings):
    str = input("input a string: ")
    valid = validators.url(str)
    if valid == True:
        lst_of_valid_url.append(str)
    else:
        print(str," isn't a link")





print(lst_of_valid_url)


