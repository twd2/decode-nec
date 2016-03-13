import sys

def get_code(a, b):
    if a < 1000:
        if abs(a - b) > 10000:
            return 'C'
        elif abs(a - b) > 500:
            return '1'
        else:
            return '0'
    elif abs(a - b) > 4000:
        return 'S'
    else:
        return 'F' # fault

def decode(code_raw):
    code = []
    for c in code_raw:
        if c < 30000:
            code.append(c)
        else:
            print(c)
            break
    # print(code)

    # print(len(code))
    codes = [(code[i], code[i + 1]) for i in range(0, len(code) - 1, 2)]
    # print(codes)

    bits = [get_code(*c) for c in codes]
    return "".join(bits)

if __name__ == '__main__':
    bits_str = decode(map(int, sys.stdin.read().split()))
    print((bits_str, len(bits_str)))