import os


def birthdayCakeCandles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles_input = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles_input)
    fptr.write(str(result) + '\n')
    fptr.close()
