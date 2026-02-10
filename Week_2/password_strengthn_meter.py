password = input("Enter password: ")

length_ok = len(password) >= 8
has_digit = False
has_upper = False
has_special = False

special_chars = "!@#$%^&*()-_+=<>?/"

for ch in password:
    if ch.isdigit():
        has_digit = True
    elif ch.isupper():
        has_upper = True
    elif ch in special_chars:
        has_special = True

print("Password check results:")
print("Length >= 8:", length_ok)
print("Contains digit:", has_digit)
print("Contains uppercase:", has_upper)
print("Contains special character:", has_special)

if length_ok and has_digit and has_upper and has_special:
    print("Password is STRONG")
else:
    print("Password is WEAK")