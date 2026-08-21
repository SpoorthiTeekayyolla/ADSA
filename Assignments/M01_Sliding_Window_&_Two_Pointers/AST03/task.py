# task.py

def countGoodSubstrings(s: str) -> int:
    count = 0

    # Check every substring of length 3
    for i in range(len(s) - 2):
        substring = s[i:i + 3]

        # A good substring has 3 distinct characters
        if len(set(substring)) == 3:
            count += 1

    return count


if __name__ == '__main__':
    s = input()
    print(countGoodSubstrings(s))