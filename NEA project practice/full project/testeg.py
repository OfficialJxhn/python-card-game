max = 0
lst = []
max_list = []
string = ""
amount_of_digits = int(input("Enter the amount of digits you want: "))
for i in range(amount_of_digits):
    number_to_add = int(input("Enter the digit: "))
    lst.append(number_to_add)

for j in lst:
    freq = lst.count(j)
    lst.remove(j)
    print(lst)
    if freq > max and freq != max:
        max = freq
        max_list.clear()
        max_list.append(max)
    elif freq == max: 
       print("Data was multimodal")
       quit()
    else:
        continue

print(f"the modal digit came up {max} times")