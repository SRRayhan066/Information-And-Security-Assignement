# AES Encryption/Decryption

### Prequisite
For making this whole programm runnable,there is something that need to be imported first.   
By using this command,
```
pip install cryptography
```
<img src="./images/cryptographyInstall.png">

### Generating AES Key

For encryption and decryption, we need to generate an AES key. That’s why for 128 bits we create an AES key named `aes_key.bin`.
 
<img src="./images/aes_key_generated.png">  

The generated `aes_key.bin` looks like this,

<img src="./images/aes_key.png">

### ECB Mode

#### <b>Encryption using 128 Bits.</b>

After that, we have created an input.txt file and encrypt it using ECB 128 bits.

<img src="./images/ECB_128_encryption.png">

The encrypted file look like this,            

<img src="./images/ECB_128_encryption_file.png">



#### <b>Decryption using 128 bits</b>

After decryption,      

<img src="./images/ECB_128_decryption.png">

The decryption file,        

<img src="./images/ECB_128_decryption_file.png">


