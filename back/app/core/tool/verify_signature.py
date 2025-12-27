import binascii

from ecdsa import VerifyingKey, SECP256k1, BadSignatureError

def verify_signature(public_key_hex: str, tx_hash_hex: str, signature_hex: str) -> bool:
    try:
        vk = VerifyingKey.from_string(
            binascii.unhexlify(public_key_hex),
            curve=SECP256k1
        )
        vk.verify(
            binascii.unhexlify(signature_hex),
            binascii.unhexlify(tx_hash_hex)
        )
        return True
    except BadSignatureError:
        return False
