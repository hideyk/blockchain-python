**Activate the virtual environment**

```
activate /venv/Scripts
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```


**Run the application and API**

Make sure to activate the virtual environment

```
python -m backend.app
```

**Run a peer instance**
 
```
export PEER=True && python -m backend.app
```
hello

---

# Chain Validation & Chain Replacement

## Chain Validation
1. Correct fields (Hash, last hash, timestamp, data)
2. Must correctly reference the hash of the last block
3. Valid hash
4. Valid Proof Of Work (Same no. of leading 0s as difficulty)

## Chain Replacement
- As long as new chain is longer, incoming chain is valid
- Necessary as multiple instances of blockchain --> Blockchain network will come to unanimous agreement on official set of blocks
- No central authority to validate authenticity of blocks