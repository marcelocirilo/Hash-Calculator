import hashlib

class Calculator():
    
    def __init__(self,file_path,hash_algorithm):
        self.file_path=file_path
        self.hash_algorithm=int(hash_algorithm)
    
    def hash(self):
        match self.hash_algorithm:
            case 1:
                return 'md5'
            case 2:
                return 'sha224'
            case 3:
                return 'sha256'
            case 4:
                return 'sha384'
            case 6:
                return 'sha512'
            case 6:
                return 'sha3_224'
            case 7:
                return 'sha3_256'
            case 8:
                return 'sha3_384'
            case 9:
                return 'sha3_512'
            case _:
                raise ValueError("Invalid algorithm choice.")
        
    def calculator(self):
        hash_choice=self.hash()
        hash_func = getattr(hashlib, hash_choice)

        try:
            with open(self.file_path, "rb") as f:
                file_hash = hash_func(f.read()).hexdigest()
                print(f"Hash ({hash_choice}) of the file: {file_hash}")
        except FileNotFoundError:
            print("File not found. Please check the file path.")
    
    
    
