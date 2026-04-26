# Loop numbers and stop when number > 6.
# Expected output 0 - 6

for number in range(15):
    if number > 6:
        break
    print(number)
print('-------------------')
for number in range(10):
    if number == 4:
        continue
    print(number)

if False:
    pass