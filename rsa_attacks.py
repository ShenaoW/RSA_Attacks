from attacks.common_modulus import *
from attacks.common_factor import *
from attacks.small_crt_exp import *
from attacks.fermat_fac import *
from attacks.pollard_p_1 import *


def frame_parser():
    n_list = []
    e_list = []
    c_list = []
    for i in range(21):
        with open("RSA大礼包\附件3-2（发布截获数据）\Frame" + str(i), "r") as f:
            file_data = f.read()
            n_list.append(file_data[0:256])
            e_list.append(file_data[256:512])
            c_list.append(file_data[512:768])
    return n_list, e_list, c_list


if __name__ == "__main__":
    N, E, C = frame_parser()

    # Common Modulus Attack
    print(common_modulus(N, E, C))

    '''
    Common Modulus Found! —— > Frame0 and Frame4
    [b'My secre']
    '''

    # Common Factor Attack
    # print(common_factor(N, E, C))

    '''
    Common Factor Found! ——> Frame1 and Frame18
    [b'. Imagin', b'm A to B']
    '''

    # Small Exponent Attack
    # small_exp_check(E)
    # print(small_crt_exp(N, E, C))

    '''
    Frame 3 has a small exponent:5
    Frame 7 has a small exponent:3
    Frame 8 has a small exponent:5
    Frame 11 has a small exponent:3
    Frame 12 has a small exponent:5
    Frame 15 has a small exponent:3
    Frame 16 has a small exponent:5
    Frame 20 has a small exponent:5
    [b'\xb8\xbc\xa2S)s\xcd\xd2', b't is a f']
    exp3 ——> b'\xb8\xbc\xa2S)s\xcd\xd2'
    exp5 ——> b't is a f'
    '''

    # Fermat Factorization Attack
    # print(fermat_fac(N, E, C))

    '''
    Fermat Factorization Succeed! ——> Frame10
    [b'will get']
    '''

    # Pollard p-1 Attack
    # print(pollard_p_1(N, E, C))

    '''
    p of Frame2 is : 1719620105458406433483340568317543019584575635895742560438771105058321655238562613083979651479555788009994557822024565226932906295208262756822275663694111
    p of Frame6 is : 920724637201
    p of Frame19 is : 1085663496559
    [b' That is', b' "Logic ', b'instein.']
    '''



