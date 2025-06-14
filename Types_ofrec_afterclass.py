def has_negative(lst):

   if not lst:
      return False

   if lst[0] < 0:
      return True

   return has_negative(lst[1:])

numbers = [3, 5, -7, 2]

if has_negative(numbers):
   print("The list contains a negative number.")
else:
   print("The list does not contain any negative numbers.")