import time
from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

publish_key = "pub-c-c73a7b6c-a9d3-427d-a4cb-d581b4f80bd3"
subscribe_key = "sub-c-cf130334-2974-11ec-b8a4-52e976b77916"

pnconfig = PNConfiguration()
pnconfig.publish_key = publish_key 
pnconfig.subscribe_key = subscribe_key

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION'
}

class Listener(SubscribeCallback):
    """
    Extended class overrides behaviour to occur in response to certain events.
    """
    def __init__(self, blockchain, transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print(f'\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')

        elif message_object.channel == CHANNELS['TRANSACTION']:
            transaction = Transaction.from_json(message_object.message)
            self.transaction_pool.set_transaction(transaction)


class PubSub():
    """
    Handles the publish/subscribe layer of the application
    Provides communication between the nodes of the blockchain network
    """
    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self, channel, message):
        """
        Publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

    def broadcast_transaction(self, transaction):
        """
        Broadcast a transaction to all nodes.
        """
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())


def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})


if __name__ == "__main__":
    main()