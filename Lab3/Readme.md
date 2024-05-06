# Task 1

### Using aes-128-cbc :

<b>Encryption Code :</b>
```
openssl enc -aes-128-cbc -e  -in Task1.txt -out Task1-aes-128-cbc.bin \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

<b>Decryption Code :</b>
```
openssl enc -aes-128-cbc -d  -in Task1-aes-128-cbc.bin \
                            -out   decryptedTask1-aes-128-cbc.txt \
                            -K  00112233445566778889aabbccddeeff \
                            -iv 01020304050607083241231213124f23
```

### Using aes-128-ebc :

<b>Encryption Code :</b>
```
openssl enc -aes-128-ebc -e  -in Task1.txt -out Task1-aes-128-ebc.bin \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

<b>Decryption Code :</b>
```
openssl enc -aes-128-ebc -d  -in Task1-aes-128-ebc.bin \
                            -out   decryptedTask1-aes-128-ebc.txt \
                            -K  00112233445566778889aabbccddeeff \
                            -iv 01020304050607083241231213124f23
```

### Using aes-128-ecb :

<b>Encryption Code :</b>
```
openssl enc -aes-128-ecb -e  -in Task1.txt -out Task1-aes-128-ecb.bin \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

<b>Decryption Code :</b>
```
openssl enc -aes-128-ecb -d  -in Task1-aes-128-ecb.bin \
                            -out   decryptedTask1-aes-128-ecb.txt \
                            -K  00112233445566778889aabbccddeeff \
                            -iv 01020304050607083241231213124f23
```




## Task 3
```
openssl enc -aes-128-ecb -e  -in Task3.txt -out encryptedTask3-ecb.bin -K 2019831066010203040506070809aabb
```


```
openssl enc -aes-128-ecb -d  -in encryptedTask3-ecb.bin -out decryptedTask3-ecb.txt -K 2019831066010203040506070809aabb
```