# File Hash Calculator
 
A Python script that calculates the hash of a file using various hashing algorithms available in the hashlib library. This tool is useful for verifying file integrity and ensuring that files have not been altered.

##Features
Dynamically select hashing algorithms:
md5
sha224
sha256
sha384
sha512
sha3_224
sha3_256
sha3_384
sha3_512
Supports user input for file path and hash algorithm selection.
Uses Python's getattr to dynamically choose the hashing algorithm.

##Requirements
Python 3.8 or higher

##Installation
Clone the repository:

bash
Copiar
Editar
git clone https://github.com/your-username/file-hash-calculator.git
cd file-hash-calculator
Install Python if not already installed: Python Downloads

Usage
Run the script:

bash
Copiar
Editar
python main.py
Enter the required inputs:

File path: Provide the full path to the file you want to hash.
Choose the hashing algorithm by entering the corresponding number (e.g., 1 for md5, 2 for sha224, etc.).
The script will display the selected hash algorithm and calculate the hash for the given file.

Example
Input:
plaintext
Copiar
Editar
Enter a file path: /path/to/your/file.txt
Choose an algorithm:
 1. md5
 2. sha224
 3. sha256
 4. sha384
 5. sha512
 6. sha3_224
 7. sha3_256
 8. sha3_384
 9. sha3_512
> 3
Output:
plaintext
Copiar
Editar
File Path: /path/to/your/file.txt
Hash Algorithm: sha256
File Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b53d94a1c171d7d62
How It Works
Dynamic Algorithm Selection: The script uses getattr to dynamically fetch the selected hash algorithm from the hashlib library. For example:

python
Copiar
Editar
hash_func = getattr(hashlib, hash_choice)
Hash Calculation: The chosen algorithm is applied to the file's content to compute its hash.

Output: The computed hash is displayed in hexadecimal format.

Code Overview
main.py
Handles user input, initializes the Calculator object, and prints the results.

calculator.py
Contains the Calculator class with methods to:

Parse the hashing algorithm.
Compute the hash for the given file.
Limitations
The script assumes the file exists and is accessible. If the file path is invalid, it will throw an error.
The input for the hashing algorithm must be numeric and within the range of options.
Contributing
Fork the repository.
Create a feature branch: git checkout -b feature-name
Commit your changes: git commit -m 'Add feature'
Push the branch: git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.