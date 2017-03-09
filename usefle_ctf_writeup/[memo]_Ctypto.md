- RSA

    - Crack private key password
        https://github.com/Ne0Lux-C1Ph3r/WRITE-UP/blob/master/Nullcon_HackIM/cryptopuzzle3.md
        JohnTheRipper/run/john --stdout --incremental | ./ssh-privkey-crack ~/Desktop/VM-Share/20170211_nullconCTF/next-setp/HackIM.key

    - Decrypt encryption file by RSA
        $ openssl rsa -in in_keyfile -text
         -> display key information
        $ openssl rsautl -in in_file -out out_file -inkey in_keyfile
    - make private pem file from p,q,n,e
        $ /opt/share/rsatool/rsatool.py -p P -q Q -o out.pem
    - Decrypt encryption file by AES
        $ openssl 

    - Caluculate p,q from N
        - Sympy.factorint()
        - factordb http://factordb.com/
        - use RSAtool https://github.com/sourcekris/RsaCtfTool

    - decrypt ssl packet in wireshark  (example: https://ctf.rip/bsides-sf-ctf-2017-root-crypto-challenge/)
        1. find RSA public key in Server hello, and extract it
        2. calculate P,Q by using Sympy.factorint, etc
        3. make PEM file by using rsatool
        4. import PEM file in wireshark  mark down SSL packet, right click, choose protocol Preference->RSA Key list -> fill out list.
        5. mark down SSL decrypted packet(you can see HTTP packet instead of SSL packet), right click, choose follow -> SSL stream. 

- Hash
    - length extention attack

    - Rainbow table (Web site)

- AES
    - Cipher text looks Ascii text but can decrypt it.
        https://blog.skullsecurity.org/2016/going-the-other-way-with-padding-oracles-encrypting-arbitrary-data
        https://github.com/ginjabenjamin/CTF/tree/master/BsidesSF/CR/in-plain-sight
            >>> import binascii
            >>> from Crypto.Cipher import AES
            >>> k = binascii.unhexlify('c086e08ad8ee0ebe7c2320099cfec9eea9a346a108570a4f6494cfe7c2a30ee1')
            >>> iv = binascii.unhexlify('0a0e176722a95a623f47fa17f02cc16a')
            >>> c = 'HiddenCiphertext'
            >>> aes = AES.new(k, AES.MODE_CBC, iv)
            >>> aes.decrypt(c)
'           FLAG:1d010f248d\x01'

- Ceaser encryption


