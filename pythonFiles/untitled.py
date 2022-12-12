# Write your large_power function here:
def large_power(int b, int exponent):
  result = false
  total = b**exponent

  if (total>5000)
    result =true
  
  return result
    
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False