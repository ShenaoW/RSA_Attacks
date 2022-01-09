from attacks.crt import *
import gmpy2 as gp


def small_exp_check(e_list):
    small_exp = []
    index = []
    for i in range(len(e_list)):
        e = int(e_list[i], 16)
        if e < 10:
            small_exp.append(e)
            index.append(int(i))
            # print("Frame " + str(i) + " has a small exponent:" + str(e))
    return index, small_exp


'''
Frame 3 has a small exponent:5
Frame 7 has a small exponent:3
Frame 8 has a small exponent:5
Frame 11 has a small exponent:3
Frame 12 has a small exponent:5
Frame 15 has a small exponent:3
Frame 16 has a small exponent:5
Frame 20 has a small exponent:5
'''


def small_crt_exp(n_list, e_list, c_list):
    index, small_exp = small_exp_check(e_list)
    c_list_exp3 = []
    n_list_exp3 = []
    c_list_exp5 = []
    n_list_exp5 = []
    result = []
    # exp 3
    for i in range(len(index)):
        if small_exp[i] == 3:
            c_list_exp3.append(int(c_list[index[i]], 16))
            n_list_exp3.append(int(n_list[index[i]], 16))
    m3 = gp.iroot(crt(c_list_exp3, n_list_exp3), 3)

    # exp 5
    for i in range(len(index)):
        if small_exp[i] == 5:
            c_list_exp5.append(int(c_list[index[i]], 16))
            n_list_exp5.append(int(n_list[index[i]], 16))
    m5 = gp.iroot(crt(c_list_exp5, n_list_exp5), 5)

    result.append(bytes.fromhex(hex(m3[0])[-16:]))
    result.append(bytes.fromhex(hex(m5[0])[-16:]))
    return result
