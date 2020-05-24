new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
				{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# import sha256
from hashlib import sha256
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 3
nonce = 0
# creating the proof 
text = str(nonce)+str(new_transactions)
proof = sha256(text.encode()).hexdigest()
# printing proof
print(proof)
  
# finding a proof that has 2 leading zeros
while not str(proof[:2]) == "0"*difficulty:
	nonce +=1
	text = str(nonce)+str(new_transactions)
	proof = sha256(text.encode()).hexdigest()
	print(proof)


# printing final proof that was found
final_proof = proof
print("final proof ",final_proof," nonce ",nonce)
