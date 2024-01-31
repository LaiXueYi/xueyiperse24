numbers = []
for i in range(12):
  num = input()
  numbers += [num]

valid_nums = 0
for nums in numbers:
  if int(nums[-1]) == int(nums[0]) + 1:
    valid_nums += 1
  elif int(nums[-1]) == int(nums[0]) - 1:
    valid_nums += 1
print(valid_nums)
    
