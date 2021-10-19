import hashlib
import json

def crypto_hash(*args):
    """
    Return a SHA-256 hash of the given data
    """
    stringified_args = map(json.dumps, args)
    joined_args = '^'.join(stringified_args)
    
    return hashlib.sha256(joined_args.encode('utf-8')).hexdigest()


def main():
    print(f"Crypto_hash('foo'): {crypto_hash('foo')}")
    print(f"Crypto_hash(1): {crypto_hash(1)}")
    print(f"Crypto_hash(['foo']): {crypto_hash(['foo'])}")
    print(f"Crypto_hash('arg', 'bae'): {crypto_hash('arg', 'bae')}")
    print(f"Crypto_hash('bae', 'arg'): {crypto_hash('bae', 'arg')}")
    print(f"Crypto_hash('arg', ['bae']): {crypto_hash('arg', ['bae'])}")


if __name__ == "__main__":
    main()