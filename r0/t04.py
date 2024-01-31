input1 = input()
input2 = input()
input3 = input()
if input1 != input2:
  if input1 == input3:
    print("ENTRY 2 MISMATCH")
  elif input1 != input3:
    print("BOTH MISMATCH")
elif input1 != input3:
  print("ENTRY 3 MISMATCH")
else:
  print("OK")
  
