# Simple Blockchain written in python

import hashlib
import json
import time

class Blockchain:

    def __init__(self):
        self.block = []
        self.pending = []
        self.transactions = []
        self.add_block(prevhash="Genesis", proof = 123)

    def add_transaction(self, sender, receiver, amount):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }
        self.pending.append(transaction)

    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()
        main_hash = hashlib.sha256(json_block).hexdigest()
        return main_hash

    def add_block(self, proof, prevhash = None):
        block = {
            "index":len(self.block),
            "timestamp": time.time(),
            "transactions":self.pending,
            "proof": proof,
            "prevhash": prevhash or self.compute_hash(self.block[-1])
        }

        self.pending = []
        self.block.append(block)


# testing features
blockchain = Blockchain()
t1 = blockchain.add_block(123)
t2 = blockchain.add_block(123)
print(blockchain.block)
t3 = blockchain.add_block(345)
print(blockchain.block)

transaction = blockchain.add_transaction("rahul", "ram", 233)
hash = blockchain.compute_hash(3)
my_block = blockchain.add_block(789, hash)

print(blockchain.block)

