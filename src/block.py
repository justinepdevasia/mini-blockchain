from datetime import datetime
from hashlib import sha256

class Block:
	def __init__(self,transactions,prev_hash,nonce=0):
		self.transactions = transactions
		self.prev_hash = prev_hash
		self.nonce = nonce
		self.timestamp = datetime.now()
		self.hash = self.generate_hash()

	def generate_hash(self):
		block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
		block_hash_result = sha256(block_contents.encode())
		return block_hash_result.hexdigest()
