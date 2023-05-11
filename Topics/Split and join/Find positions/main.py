# put your python code here
user_input = input().split(" ")
number_find = input()

lst = []
ans = [i for i, x in enumerate(user_input) if x == number_find]
if len(ans) > 0:
    print(*ans)
else:
    print("not found")