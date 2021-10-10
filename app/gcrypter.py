# ******************************************************************************
#  (c) 2019-2021 Nurul-GC.                                                     *
# ******************************************************************************
"""
GCrypter-API
"""
from secrets import token_bytes


def encrypt(t: str):
    """funcao encriptadora"""
    encriptar = t.encode()
    encriptar_ = token_bytes(len(t))

    encriptado = int.from_bytes(encriptar, 'big')
    encriptado_ = int.from_bytes(encriptar_, 'big')

    encriptado_final = encriptado ^ encriptado_
    return encriptado_final, encriptado_


def decrypt(v1: int, v2: int):
    """funcao desencriptadora"""
    palavra_encriptada = int(v1) ^ int(v2)
    desencriptada = palavra_encriptada.to_bytes((palavra_encriptada.bit_length() + 7) // 8, 'big')
    return desencriptada.decode()
