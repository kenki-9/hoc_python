def get_min_number(numbers):

  result = numbers[0]
  for num in numbers:
    if result > num:
      result = num
  return result


numbers = [10, 5, 2, 7, 8, 3, 1]

min_number = get_min_number(numbers)

print("Min number: ", min_number)