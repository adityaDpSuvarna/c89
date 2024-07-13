from flask import Flask, render_template, request
import os
from time import time
from blockchain import BlockChain, Block

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

chain = BlockChain()
#Set currentBlock to none to show no block is created yet
currentBlock = None

@app.route("/", methods= ["GET", "POST"])
def home():
    # Access currentBlock as global
    global blockData, currentBlock, chain
         
    if request.method == "GET":
        return render_template('index.html')
    else:
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        landId = request.form.get("landId")
        lattitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        area = request.form.get("area")
        amount = request.form.get("amount")
        
        transaction = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount,
                "landId": landId,  
                "latitude": lattitude,
                "longitude": longitude,
                "area": area          
            }  

        index = chain.length()
        if index==0:
            index = 1

        blockData = {
                'index': index,
                'timestamp': time(),
                'previousHash': "No Previous Hash.",
        }   

        # If no block then create new block
        
            # Remove passing transaction to Block() constructor and move it inside the if condition
        currentBlock = Block(
                        blockData["index"], 
                        blockData["timestamp"], 
                        blockData["previousHash"],
                        blockData['transaction'] )



        
        # Receive status of the currentBlock.
        currentBlock.addTransactions(transaction)

        # Check block status after adding transaction, if block is ready then add the block to the blockchain
        # and make currentBlock variable None 
        
        chain.addBlock(currentBlock)   
        isValid = chain.validateBlock(currentBlock)
        currentBlock.isValid = isValid


            # Set currentBlock to none
        currentBlock= None
        
        chain.printChain()

    
    return render_template('index.html', blockChain = chain)


@app.route("/blockchain", methods= ["GET", "POST"])
def show():
    global chain, currentBlock

    currentBlockLength  = 0
    if currentBlock:
        currentBlockLength = len(currentBlock.transactions)
    
    return render_template('blockchain.html', blockChain = chain.chain, currentBlockLength = currentBlockLength)


if __name__ == '__main__':
    app.run(debug = True, port=4001)