import gmpy2
import binascii


def pp1(n):
    B = 2 ** 20
    a = 2
    for i in range(2, B + 1):
        a = pow(a, i, n)
        d = gmpy2.gcd(a - 1, n)
        if (d >= 2) and (d <= (n - 1)):
            q = n // d
            n = q * d
    return d


def pollard_p_1(n_list, e_list, c_list):
    index_list = [2, 6, 19]
    plaintext = []
    for i in range(3):
        N = int(n_list[index_list[i]], 16)
        c = int(c_list[index_list[i]], 16)
        e = int(e_list[index_list[i]], 16)
        p = pp1(N)
        print("p of Frame" + str(index_list[i]) + " is : " + str(p))
        q = N // p
        phi_of_frame = (p - 1) * (q - 1)
        d = gmpy2.invert(e, phi_of_frame)
        m = gmpy2.powmod(c, d, N)
        plaintext.append(binascii.a2b_hex(hex(m)[-16:]))
    return plaintext
