'''
Main class for Lucid Technical Assessment, from which everything will be executed.

@author: Pedro
'''
from lucid.challenge.io import InputReader
import sys

if __name__ == '__main__':
    
    # Read user input
    reader = InputReader()
    tasks = reader.read(sys.stdin)
    
    for task in tasks:
        print(task.command)
