num = int(input("Enter your number: "))
rev_binary = ""
binary = ""
while num != 0:
    ans = num % 2
    num = num // 2
    rev_binary = rev_binary + str(ans)

for i in range(1,len(rev_binary)+1):
    binary = binary + rev_binary[-i]

print(binary)
