# To find the max - functionc - prebuilt functions
num1=int(input("Enter num1 :"))
num2=int(input("Enter the num2:"))
Maxresult = max(num1, num2)
power=pow(num1,num2)


#result = max(3, "pramod") - Data Types

# print(f"Maximum of two numbers: {max(num1, num2)}")
#
# #print(f"{table}*1={table}")
# #print("Power is ",pow(num1,num2))
# print(f"Power of two number is : {pow(num1,num2)}")
# print(f"Sum of two number is : ",f"{num1+num2}=")
# print("Sub is ", f"{num1}-{num2}={num1-num2}")
# print("Mul is ", f"{num1}*{num2}={num1*num2}")

maximum = max(num1, num2)
power = num1 ** num2
subtraction = num1 - num2
multiplication = num1 * num2
addition = num1 + num2
division = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"

# Print results using f-string formatting
print(f"\nResults:")
print(f"Maximum: {maximum}")
print(f"{num1} raised to the power of {num2}: {power}")
print(f"Subtraction (num1 - num2): {subtraction}")
print(f"Multiplication (num1 * num2): {multiplication}")
print(f"Addition (num1 + num2): {addition}")
print(f"Division (num1 / num2): {division}")
