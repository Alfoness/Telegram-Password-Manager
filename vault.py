import json

class Vault:
    def __init__(self, notes: tuple):
        self.notes = notes
    
    def stdout(self) -> dict:
        ...