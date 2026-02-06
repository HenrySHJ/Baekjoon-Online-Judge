arr = [""] * 3

ans = 0
for i in range(3):
    x = input()

    if x != "Fizz" and x != "Buzz" and x != "FizzBuzz":
        ans = int(x) + 3 - i

if ans % 3 == 0 and ans % 5 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else:
    print(ans)