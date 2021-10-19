from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # It should create the same output given same input --> Deterministic
    assert crypto_hash(1, [3]) == crypto_hash(1, [3])
    assert crypto_hash('foo') == 'b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b'