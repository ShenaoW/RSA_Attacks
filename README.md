# RSA_Attacks
2016年全国高校密码数学挑战赛的赛题三——RSA加密体制破译

RSA大礼包中存放原赛题数据

attacks文件夹下存放相关破解算法

调用 rsa_attacks.py 以运行



###  Attacks with single_key 

**低加密指数攻击 (Small Crt Exp Attack)：** 利用中国剩余定理，现代密码学（杨波）P118

```
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
```

**费马分解 (Fermat Fac Attack)：**[CTF Wiki 模数相关攻击 |p-q|较小](https://ctf-wiki.org/crypto/asymmetric/rsa/rsa_module_attack/#p-q)

```
Fermat Factorization Succeed! ——> Frame10
[b'will get']
```

**Pollard p-1 Attack ：**[CTF Wiki 模数相关攻击 p-1光滑](https://ctf-wiki.org/crypto/asymmetric/rsa/rsa_module_attack/#p-1)

```
p of Frame2 is : 1719620105458406433483340568317543019584575635895742560438771105058321655238562613083979651479555788009994557822024565226932906295208262756822275663694111
p of Frame6 is : 920724637201
p of Frame19 is : 1085663496559
[b' That is', b' "Logic ', b'instein.']
```

### Attacks with multi_keys

**共模攻击（Common Modulus Attack）：**[CTF Wiki 模数相关攻击 共模攻击](https://ctf-wiki.org/crypto/asymmetric/rsa/rsa_module_attack/#_7)

```
Common Modulus Found! —— > Frame0 and Frame4
[b'My secre']
```

**因数碰撞（Common Factor Attack）：**[CTF Wiki 模数相关攻击 模不互素](https://ctf-wiki.org/crypto/asymmetric/rsa/rsa_module_attack/#_5)

```
Common Factor Found! ——> Frame1 and Frame18
[b'. Imagin', b'm A to B']
```



最终仍有5个Frame无法恢复，分别是5,9,13,14,17

通过猜测获得最终明文：

```
"My secret is a famous saying of Albert Einstein. That is \"Logic will get you from A to B. Imagination will take you everywhere.\""
```

