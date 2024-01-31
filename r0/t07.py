totalwords = int(input())
interactions = 0
learnt = 0

while totalwords >= 5:
  totalwords -= 5
  interactions += learnt + 5
  learnt += 5
interactions += learnt + totalwords
print(interactions)
  
