from Crypto.Util.number import inverse, long_to_bytes
from binascii import a2b_hex

# 拓展Euclid
def extend_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = extend_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def common_modulus(n_list, e_list, c_list):
    index1 = []
    index2 = []
    result = []
    for i in range(len(n_list)):
        for j in range(i + 1, len(n_list)):
            if n_list[i] == n_list[j]:
                index1.append(i)
                index2.append(j)
                print("Common Modulus Found! ——> Frame" + str(i) + " and Frame" + str(j))
    for i in range(len(index1)):
        n = int(n_list[index1[i]], 16)
        e1 = int(e_list[index1[i]], 16)
        e2 = int(e_list[index2[i]], 16)
        c1 = int(c_list[index1[i]], 16)
        c2 = int(c_list[index2[i]], 16)
        r, s, gcd = extend_gcd(e1, e2)
        result.append(bytes.fromhex(hex(pow(c1, r, n) * pow(c2, s, n) % n)[-16:]))
        # print(r, s)
        # result.append(pow(c1, r, n) * pow(c2, s, n) % n)
    return result
