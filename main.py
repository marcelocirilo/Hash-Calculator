from calculator import Calculator


file_path=input('Enter a file path:')

hash_algorithm=input('Choose an algorithm:\n 1. md5\n 2. sha224\n 3. sha256\n 4. sha384\n 5. sha512\n 6. sha3_224\n 7. sha3_256\n 8. sha3_384\n 9. sha3_512\n')

Hah=Calculator(file_path,hash_algorithm)
Hah.calculator()