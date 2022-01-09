from Crypto.Util.number import *


def common_factor(n_list, e_list, c_list):
    index1 = []
    index2 = []
    p_list = []
    result = []
    for i in range(len(n_list)):
        for j in range(i + 1, len(n_list)):
            p = GCD(int(n_list[i], 16), int(n_list[j], 16))
            if p != 1 and n_list[i] != n_list[j]:
                index1.append(i)
                index2.append(j)
                p_list.append(p)
                print("Common Factor Found! ——> Frame" + str(i) + " and Frame" + str(j))
    for i in range(len(index1)):
        n1 = int(n_list[index1[i]], 16)
        n2 = int(n_list[index2[i]], 16)
        q1 = n1 // p_list[i]
        q2 = n2 // p_list[i]
        print("q of Frame " + str(index1[i]) + " is " + str(q1))
        print("q of Frame " + str(index2[i]) + " is " + str(q2))
        e1 = int(e_list[index1[i]], 16)
        e2 = int(e_list[index2[i]], 16)
        c1 = int(c_list[index1[i]], 16)
        c2 = int(c_list[index2[i]], 16)
        phi1 = (p_list[i] - 1) * (q1 - 1)
        phi2 = (p_list[i] - 1) * (q2 - 1)
        d1 = inverse(e1, phi1)
        d2 = inverse(e2, phi2)
        m1 = pow(c1, d1, n1)
        m2 = pow(c2, d2, n2)
        result.append(bytes.fromhex(hex(m1)[-16:]))
        result.append(bytes.fromhex(hex(m2)[-16:]))
    return result
