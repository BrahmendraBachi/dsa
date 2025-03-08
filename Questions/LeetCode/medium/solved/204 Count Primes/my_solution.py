def countPrimes(n: int) -> int:
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for num in range(2, int(n ** 0.5) + 1):  # Check only up to sqrt(n)
        if is_prime[num]:
            # Mark multiples starting from num^2
            for multiple in range(num * num, n, num):
                is_prime[multiple] = False

    return sum(is_prime)  # Count the True values
