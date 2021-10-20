import pytest
import time
from backend.blockchain.block import Block, GENESIS_DATA
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE, SECONDS

def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data, 'test-miner')

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert hex_to_binary(block.hash)[0:block.difficulty] == '0' * block.difficulty

def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    
    for k, v in GENESIS_DATA.items():
        assert getattr(genesis, k) == v

def test_quickly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo', 'test-miner')
    mined_block = Block.mine_block(last_block, 'bar', 'test-miner')

    assert mined_block.difficulty == last_block.difficulty + 1
    
def test_slowly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo', 'test-miner')
    
    time.sleep(MINE_RATE / SECONDS)
    
    mined_block = Block.mine_block(last_block, 'bar', 'test-miner')

    assert mined_block.difficulty == last_block.difficulty - 1

def test_mined_block_limits_at_1():
    last_block = Block(
        time.time_ns(),
        'test_last_hash',
        'test_hash',
        'test_data',
        'test_miner',
        1,
        0
    )

    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine_block(last_block, 'bar', 'test-miner')

    assert mined_block.difficulty == 1

@pytest.fixture
def last_block():
    return Block.genesis()

@pytest.fixture
def block(last_block):
    return Block.mine_block(last_block, 'test_data', 'test_miner')

def test_is_valid_block(last_block, block):
    Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_last_hash(last_block, block):
    block.last_hash = 'evil_last_hash'
    
    with pytest.raises(Exception, match='The block last_hash must be correct.'):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_proof_of_work(last_block, block):
    block.hash = 'fff'
    
    with pytest.raises(Exception, match='The PoW requirement is not satisfied.'):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_jumped_difficulty(last_block, block):
    block.difficulty = 100
    block.hash = f'{"0" * block.difficulty}'
    
    with pytest.raises(Exception, match='Block difficulty must only adjust by 1.'):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_block_hash(last_block, block):
    block.hash = '0000000000000aaabedd'

    with pytest.raises(Exception, match='The block has to be correct.'):
        Block.is_valid_block(last_block, block)
