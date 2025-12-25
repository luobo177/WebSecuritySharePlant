# 1. 准备一个 wallet
from back.app.core.wallet.wallet import Wallet
from ecdsa import SigningKey, SECP256k1
sk = SigningKey.generate(curve=SECP256k1)

vk = sk.verifying_key

# 转成 hex 字符串
private_key_hex = sk.to_string().hex()
public_key_hex = vk.to_string().hex()

wallet = Wallet(private_key_hex, public_key_hex)

# 2. 构造 payload
payload = {
    "attack_type": "SQL Injection",
    "target_ip": "1.2.3.4",
    "detail": {
        "param": "id",
        "payload": "' or 1=1 --"
    }
}

# 3. 创建并签名 tx
tx = wallet.create_attack_tx(payload)

