import hashlib
import time

class Block:
    def __init__(self,index,previous_hash,data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode('utf-8')).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0,"0","Genesis Block")
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self,new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

if __name__ == "__main__":
    blockchain = Blockchain()

    #add blocks to blockchain

    block1 = Block(1,"","Block 1 Data")
    blockchain.add_block(block1)

    block2 = Block(2,"","Block 2 Data")
    blockchain.add_block(block2)

    block3 = Block(3,"","Block 3 Data")
    blockchain.add_block(block3)

    #print blockchain

    for block in blockchain.chain:
        print(f"Block {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash:{block.hash}")
        print("")


