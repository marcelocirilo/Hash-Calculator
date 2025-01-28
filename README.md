# File Hash Calculator
 
A Python script that calculates the hash of a file using various hashing algorithms available in the hashlib library. This tool is useful for verifying file integrity and ensuring that files have not been altered.

## Features
Dynamically select hashing algorithms:
1. md5
2. sha224
3. sha256
4. sha384
5. sha512
6. sha3_224
7. sha3_256
8. sha3_384
9. sha3_512
    
Supports user input for file path and hash algorithm selection.
Uses Python's getattr to dynamically choose the hashing algorithm.

## Requirements
Python 3.8 or higher

## Installation
1. Clone the repository:

````bash
git clone https://github.com/your-username/file-hash-calculator.git
cd file-hash-calculator
````
2. Install Python if not already installed: Python Downloads

## Usage
1. Run the script:

```bash
python main.py
```
2. Enter the required inputs:
- File path: Provide the full path to the file you want to hash.
- Choose the hashing algorithm by entering the corresponding number (e.g., 1 for md5, 2 for sha224, etc.).
  
3. The script will display the selected hash algorithm and calculate the hash for the given file.

## Example
### Input:
```bash
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
```

### Output:
```bash
Hash (sha256) of the file: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b53d94a1c171d7d62
```

## Code Overview
### main.py
Handles user input, initializes the Calculator object, and prints the results.

### calculator.py
Contains the Calculator class with methods to:

Parse the hashing algorithm.
Compute the hash for the given file.

## Limitations
The script assumes the file exists and is accessible. If the file path is invalid, it will throw an error.
The input for the hashing algorithm must be numeric and within the range of options.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
