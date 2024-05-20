#mport the necessary libraries
import sys
from solana.rpc.api import Client
from solders.keypair import Keypair
from solana.exceptions import *
import info as stored
import time


#create a class 

class test_net:
    def __init__(self):
        '''
        initialize the class
        '''
        self.public_key=''
        self.testnet_rpc="https://api.testnet.solana.com"                      #testnet rpc url
        self.LAMPORT_AMOUNT=1000000000                                         #lamport amount
        self.client=Client(self.testnet_rpc)                                   #connect to testnet rpc 


    def generate_key(self):
        '''
        this method generates a key pair and stores it in a file named info.py
        '''
        keys=Keypair()                                                       #generate a key pair
        data=keys.to_json()
        with open("info.py","w") as f:
            f.write(f'keys={data}')                                           #store the keypair in info.py
       


        
        
        
    
    
    
    
    

    def sol_request(self):
        '''
        method that requests sol for the user from the testnet rpc
        '''
        obtained_key=Keypair.from_bytes(stored.keys)                                        #retrieve the key pair from the file 
        self.public_key=obtained_key.pubkey()                                              
        print('your public key is : ',self.public_key)
        amount=int(input("Enter lamport amount  you want to request: "))                           # prompt theuser to enter the amount of sol needed
        if amount<=0:                                                                       #check if the amount is positive
            print("Enter a positive amount ")
            self.sol_request()
        else:
            try:                                                                           #try to request the sol from the  testnet rpc
                solamount=float(amount/self.LAMPORT_AMOUNT )                                               #convert the lamport to amount
                print(f'you are requesting {solamount} SOL.....')
                self.request_sol=self.client.request_airdrop(self.public_key,amount,)
                conf=self.client.confirm_transaction(self.request_sol.value)
                print(f'{solamount}SOL has been airdroped successfully.......')
                balance=self.client.get_balance(self.public_key)
                print(f'your current balance is {balance.value/self.LAMPORT_AMOUNT} SOL' )
                
            except SolanaRpcException as e:                                                #exception handler
                print('Error: too many requests has been made \nTry again after some time',e)
                sys.exit(1)
            print(f'Please check your balance' )
            
        
        
        
        
        
    def get_balance(self):
        '''
        this method is responsible for getting the balance of the user from the testnet rpc
        '''
        obtained_key=Keypair.from_bytes(stored.keys)                                     #retrieve the keypair
        self.public_key=obtained_key.pubkey()
        balance=self.client.get_balance(self.public_key)
        print(f'your current balance is  {balance.value/self.LAMPORT_AMOUNT}SOL' )
        
        
        
        
        
        
        


if __name__=="__main__":                                                                    #run the progrm
    test=test_net()
    # test.generate_key()
    # test.sol_request()
    # test.get_balance()
