import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if (ord(plaintext[i])<=ord('z') and ord(plaintext[i])>=ord('a')
            if ord(plaintext[i])>=ord('x'):
                ciphertext+=chr((ord(plaintext[i])+2)%ord('z')+ord('a'))
            else:
                ciphertext+=chr(ord(plaintext[i])+3)
        elif (ord(plaintext[i])<=ord('Z') and ord(plaintext[i])>=ord('A')):
            if ord(plaintext[i])>=ord('X'):
                ciphertext+=chr((ord(plaintext[i])+2)%ord('Z')+ord('A'))
            else:
                ciphertext+=chr(ord(plaintext[i])+3)
        else:
            ciphertext+=plaintext[i]
            
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if (ord(ciphertext[i])<=ord('z') and ord(ciphertext[i])>=ord('a')):
            if ord(ciphertext[i])<=ord('c'):
                plaintext+=chr(ord(ciphertext[i])-ord('c')+ord('z'))
            else:
                plaintext+=chr(ord(ciphertext[i])-3)
        elif (ord(ciphertext[i])<=ord('Z') and ord(ciphertext[i])>=ord('A')):
            if ord(ciphertext[i])<=ord('C'):
                plaintext+=chr(-ord('C')+ord(ciphertext[i])+ord('Z'))
            else:
                plaintext+=chr(ord(ciphertext[i])-3)
        else:
            plaintext+=ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
