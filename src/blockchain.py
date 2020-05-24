from block import Block

class Blockchain:
    def __init__(self):
 	    self.chain = []
    	self.all_transactions = []
      	self.genesis_block()
    
    def genesis_block(self):
		transactions = {}
		gen_block = Block(transactions,"0")
		self.chain.append(gen_block)
		return self.chain

    def add_block(self, transactions):
	    previous_block_hash = self.chain[len(self.chain)-1].hash
	    new_block = Block(transactions,previous_block_hash)
	    self.chain.append(new_block)

	def validate_chain(self):
	    for i in range(1, len(self.chain)):
	    	current = self.chain[i]
	    	previous = self.chain[i-1]
	    	if(current.hash != current.generate_hash()):
	    		print("The current hash of the block does not equal the generated hash of the block.")
	    		return False
	    	if(current.previous_hash != previous.generate_hash()):
	    		print("The previous block's hash does not equal the previous hash value stored in the current block.")
	    		return False
	    	return True