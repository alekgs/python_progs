"""
If is odd, print Weird
If is even and in the inclusive range of 2 to 5, print Not Weird
If is even and in the inclusive range of 6 to 20, print Weird
If is even and greater > 20, print Not Weird
"""
# if __name__ == '__main__':

n = int(input().strip())
if n % 2:
    print('Weird')
else:
    if 2 <= n <= 5 or n > 20:
        print('Not Weird')
    if 6 <= n <= 20:
        print('Weird')
