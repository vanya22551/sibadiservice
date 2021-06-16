n = int(input())
if (n == 1 or n % 10 == 1) and n != 11 and n != 111:
    print(n, " программист")
elif 10 <= n <= 20 or 10 <= n % 100 <= 20 or 5 <= n <= 9 or 5 <= n % 10 <= 9 or n == 0 or n % 10 == 0:
    print(n, " программистов")
elif 2 <= n <= 4 or 32 <= n <= 34 or 2 <= n % 100 <= 4 or 2 <= n % 10 <= 4:
    print(n, " программиста")
