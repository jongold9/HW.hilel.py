def is_prime(k):
    if k < 1000:
        if k == 2 or k == 3:
            return True
        if k % 2 == 0 or k < 2:
            return False
        for i in range(3, int(k ** 0.5) + 1, 2):
            if k % i == 0:
                return False
        return True

    else:
        print("k > 1000")


print(is_prime(int(input("is_prime: "))))
