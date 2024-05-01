import re


def main():
    key = [int(x) for x in input().split()]
    decoded_message = ""
    key_length = len(key)
    while True:
        line = input()
        if line == "find":
            break

        for i in range(len(line)):
            decoded_message += chr(ord(line[i]) - key[i % key_length])

        treasure_type = re.search(r'&(.+?)&', decoded_message).group(1)
        coordinates = re.search(r'<(.+?)>', decoded_message).group(1)
        print(f"Found {treasure_type} at {coordinates}")
        decoded_message = ""


if __name__ == '__main__':
    main()
