Create a Real Estate Tracker Blockchain
=======================================

In this activity, you will learn to use the concepts learned in the class to create the real estate tracker blockchain.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10685188/C89_PCP_GIF.gif" width = "400" height = "231">


Follow the given steps to complete this activity:


1. Update the block class to create a transaction.


* Open the file blockchain.py.


* Remove the transaction parameter from the init function.

    ```sh
    def __init__(self, index, timestamp, previousHash):
    ```

* Replace transaction with empty transactions list.


    ```sh
    self.transactions = []
    ```


*  Define addTransaction method that receives transaction as parameter.


    ```sh
    def addTransaction(self, transaction):
    ```


* Check if a transaction exists.


    ```sh
    if transaction:
    ```


* Append the transaction to `self.transactions`.


    ```sh
    self.transactions.append(transaction)
    ```


* Limit the transactions and then calculate hash.


   ```sh
   if len(self.transactions) == 3:
     self.currentHash = self.calculateHash()
    ```

* Return `Ready`.

    ```sh
    return "Ready"
    ```


* Return `Add more transactions`.

    ```sh
    return "Add more transactions"
    ```


2.  Create and add the block to the chain.


* Set currentBlock to none to show no block is created yet.


    ```sh
    currentBlock = None
    ```


*  Access currentBlock as global.


    ```sh
    global blockData, currentBlock, chain
    ```


* Remove transaction key from blockData.


    ```sh
    blockData = {
            'index': index,
            'timestamp': time(),
            'previousHash': "No Previous Hash.",
    }
    ```


* If the currentBlock is set to None, then create a new block.

    ```sh
    if currentBlock == None:
    ```


* Remove passing transaction to Block() constructor and move it inside the if condition.


    ```sh
    currentBlock = Block(
                    blockData["index"],
                    blockData["timestamp"],
                    blockData["previousHash"])
    ```
       
* Receive status of the currentBlock.


    ```sh
    status = currentBlock.addTransaction(transaction)
    ```
       
* Check block status after adding a transaction. If block is ready then add the block to the blockchain.


* Set `currentBlock` variable `None`.

    ```sh
    if status == "Ready":
        chain.addBlock(currentBlock)
        isValid = chain.validateBlock(currentBlock)
        currentBlock.isValid = isValid
    ```


* Set `currentBlock` to `none`.

   	```sh
    currentBlock = None
    ```
   
* Save and run the code to check the output.
