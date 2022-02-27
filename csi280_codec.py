#!/usr/bin/python3
"""© 2022 Eli Array Minkoff"""
from string import printable, ascii_uppercase, ascii_lowercase
from random import shuffle
import secrets  # cryptographically secure pseudo-random number generation


class Codec:
    """Basic enCOder/DECoder class - just returns the plaintext"""

    def __init__(self, key):
        """Do nothing - this is a dummy"""
        if self._validate_key(key):
            self.key = key
        else:
            raise ValueError

    def encode(self, plaintext):
        """Do nothing to encrypt"""
        return plaintext

    def decode(self, cyphertext):
        """Do nothing to decrypt"""
        return cyphertext

    @staticmethod
    def _validate_key(key):
        """Return a boolean if the key is valid for this scheme"""
        return True


class SubstitutionCypher(Codec):
    """Replaces one set of characters with another.
    key is a dict containing the substitution table"""

    def encode(self, plaintext):
        """Encode the plaintext with self.key"""
        cyphertext = ''
        for c in plaintext:
            if c in self.key:
                cyphertext += self.key[c]
            else:
                cyphertext += c
        return cyphertext

    def decode(self, cyphertext):
        """Decode the cyphertext with self.key"""
        # First time called - generate reverse key mapping
        if not hasattr(self, '__reverse_key'):
            self.__reverse_key = {v: k for k, v in self.key.items()}
        plaintext = ''
        for c in cyphertext:
            if c in self.__reverse_key:
                plaintext += self.__reverse_key[c]
            else:
                plaintext += c
        return plaintext

    @staticmethod
    def _validate_key(key):
        return type(key) == dict and set(key.keys()) == set(key.values())

    @staticmethod
    def new_cypher():
        """Generate a key, then initialize a SubstitutionCypher with it"""
        pre_key = list(printable)
        shuffle(pre_key)
        new_key = dict(zip(printable, pre_key))
        return SubstitutionCypher(new_key)

    @staticmethod
    def Caeser(offset):
        """A Caeser cypher is a form of a more general substitution cypher."""
        wheel = ascii_uppercase[offset:] + ascii_uppercase[:offset]
        wheel += ascii_lowercase[offset:] + ascii_lowercase[:offset]
        new_key = dict(zip(ascii_uppercase + ascii_lowercase, wheel))
        return SubstitutionCypher(new_key)

    @staticmethod
    def new_caeser():
        """Caeser cypher with random offset"""
        return SubstitutionCypher.Caeser(secrets.randbelow(26))

    @staticmethod
    def Rot13():
        """The laziest Caeser cypher"""
        return SubstitutionCypher.Caeser(13)


class PermutationCypher(Codec):
    """Uses the plaintext message letters but rearranges their order"""

    def encode(self, plaintext):
        """Encode the plaintext with self.key"""
        ciphertext = ""
        buffer = " " * (len(plaintext) % len(self.key))
        plaintext += buffer
        cycles = len(plaintext) / len(self.key)
        for i in range(0, int(cycles)):
            block = ""
            for j in range(0, len(key)):
                block += plaintext[j + i * len(key)]

            encrypted_block = ""

            for j in key:
                encrypted_block += block[j]

            ciphertext += encrypted_block
        return ciphertext

    def decode(self, cyphertext):
        """Encode the plaintext with self.key"""
        plaintext = ""
        buffer = " " * (len(cyphertext) % len(self.key))
        cyphertext += buffer
        cycles = len(cyphertext) / len(self.key)
        for i in range(0, int(cycles)):
            block = ""
            for j in range(0, len(key)):
                block += cyphertext[j + i * len(self.key)]

            restored_block = ""
            for j in range(0, len(key)):
                for k in range(0, len(key)):
                    if j == key[k]:
                        restored_block += block[k]

            plaintext += restored_block
        return plaintext
