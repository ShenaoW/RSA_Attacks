import gmpy2 as gp
from Crypto.Util.number import *


def fac(n):
    limit = gp.iroot(n, 4)[0]
    x = gp.iroot(n, 2)[0]
    for i in range(limit):
        x += 1
        temp = pow(x, 2) - n
        if gp.is_square(temp):
            y = gp.isqrt(temp)
            p = x + y
            if x - y < 0:
                q = y - x
            else:
                q = x - y
            return p, q
    return None


def fermat_fac(n_list, e_list, c_list):
    index_fac = []
    n_fac = []
    p_list = []
    q_list = []
    result = []
    for i in range(10, 11):
        n = int(n_list[i], 16)
        if fac(n) is not None:
            p, q = fac(n)
            # q = 9686924917554805418937638872796017160525664579857640590160320300805115443578184985934338583303180178582009591634321755204008394655858254980766008932978633
            print("Fermat Factorization Succeed! ——> Frame" + str(i))
            index_fac.append(i)
            n_fac.append(n)
            p_list.append(p)
            q_list.append(p)
    for i in range(len(index_fac)):
        index = index_fac[i]
        n = n_fac[i]
        p = p_list[i]
        # q = q_list[i]
        q = 9686924917554805418937638872796017160525664579857640590160320300805115443578184985934338583303180178582009591634321755204008394655858254980766008932978633
        phi = (p - 1) * (q - 1)
        e = int(e_list[index], 16)
        c = int(c_list[index], 16)
        d = inverse(e, phi)
        m = pow(c, d, n)
        result.append(bytes.fromhex(hex(m)[-16:]))
    return result

