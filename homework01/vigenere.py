def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    keyword=keyword*(len(plaintext)//len(keyword)+1)
    for i in range(len(plaintext)):
        if (ord(plaintext[i])<=ord('z') and ord(plaintext[i])>=ord('a')):
            if ord(plaintext[i])+ord(keyword[i])-ord('a')>ord('z'):
                ciphertext+=chr(ord(plaintext[i])+ord(keyword[i])-ord('z')-1)
            else:
                ciphertext+=chr(ord(plaintext[i])+ord(keyword[i])-ord('a'))
        elif (ord(plaintext[i])<=ord('Z') and ord(plaintext[i])>=ord('A')):
            if ord(plaintext[i])+ord(keyword[i])-ord('A')>ord('Z'):
                ciphertext+=chr(ord(plaintext[i])+ord(keyword[i])-ord('Z')-1)
            else:
                ciphertext+=chr(ord(plaintext[i])+ord(keyword[i])-ord('A'))
        else:
            ciphertext+=plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    keyword=keyword*(len(ciphertext)//len(keyword)+1)
    for i in range(len(ciphertext)):
        if (ord(ciphertext[i])<=ord('z') and ord(ciphertext[i])>=ord('a')):
            if ord(ciphertext[i])-ord(keyword[i])+ord('a')<ord('a'):
                plaintext+=chr(ord(ciphertext[i])-ord(keyword[i])+ord('z')+1)
            else:
                plaintext+=chr(ord(ciphertext[i])-ord(keyword[i])+ord('a'))
        elif (ord(ciphertext[i])<=ord('Z') and ord(ciphertext[i])>=ord('A')):
            if ord(ciphertext[i])-ord(keyword[i])+ord('A')<ord('A'):
                plaintext+=chr(ord(ciphertext[i])-ord(keyword[i])+1+ord('Z'))
            else:
                plaintext+=chr(ord(ciphertext[i])-ord(keyword[i])+ord('A'))
        else:
            plaintext+=ciphertext[i]
    return plaintext
