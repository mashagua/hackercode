# Complete the solve function below.
import os
def solve(s):
    name=s.split(' ')
    name=[s.capitalize() for s in name]
    return ' '.join(name)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()