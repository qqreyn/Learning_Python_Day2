name = input("Enter your name:")
age = input("Enter how old are you:")

Age = int(age)

years = 2026 - Age
months = 12 * Age
days = 365 * Age

print("Hello", name)
print("You've been alive for:")
print(years, "Years")
print(months, "Months")
print(days, "Days")
