# Only even numbers
check = all(not int(input()) & 1 for _ in range(10))
print(('NO', 'YES')[check])
