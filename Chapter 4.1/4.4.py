for n in range(2,int(input("input a munber: "))):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break

	else:
		print(n, 'is a prime number')


# "continue" continues with the next iteration of the loop
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)