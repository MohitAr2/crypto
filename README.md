📜 Algorithms Used
1️⃣ DES (Data Encryption Standard)  📂 Path: ciphers/DES.py
  
    1️⃣ Convert plaintext to 64-bit binary blocks  
    2️⃣ Apply Initial Permutation (IP)  
    3️⃣ Split into left (L) and right (R) 32-bit halves  
    4️⃣ Perform 16 Feistel rounds:
       - Expand R to 48-bits (Expansion Permutation)  
       - XOR with round key (generated from 56-bit key)  
       - Pass through S-boxes (Substitution)  
       - Apply P-box permutation  
       - XOR with L (Swap L & R)  
    5️⃣ Apply Final Permutation (FP) to get ciphertext  


2️⃣ Playfair Cipher 📂 Path: ciphers/Play_Fair.py

    1️⃣ Prepare a 5x5 key matrix using the keyword  
    2️⃣ Split plaintext into digraphs (pairs of letters)  
    3️⃣ For each pair:
       - If letters are in the same row, replace each with the right letter  
       - If letters are in the same column, replace each with the below letter  
       - If neither, form a rectangle and swap opposite corners  
    4️⃣ Repeat for all pairs to get ciphertext  


3️⃣ Rail Fence Cipher  📂 Path: ciphers/Rail_Fence.py

    1️⃣ Choose the number of rails (key)  
    2️⃣ Write the plaintext in a zigzag pattern across rails  
    3️⃣ Read row-wise to form ciphertext  
    4️⃣ To decrypt, reconstruct the zigzag pattern using the key  


4️⃣ Hill Cipher  📂 Path: ciphers/Hill.py
    
    1️⃣ Convert plaintext to numeric values using A=0, B=1, ... Z=25  
    2️⃣ Create a square matrix as the encryption key  
    3️⃣ Multiply plaintext matrix with key matrix (mod 26)  
    4️⃣ Convert the resulting matrix back to letters to get ciphertext  

5️⃣ Row-Column Transposition Cipher  📂 Path: ciphers/Row_Column_transposition.py
    
    1️⃣ Arrange plaintext into a grid based on a key length  
    2️⃣ Read column-wise in the order defined by the key  
    3️⃣ Concatenate column-wise values to get ciphertext  


6️⃣ S-DES (Simplified DES)  📂 Path: ciphers/S-DES.py
    
    1️⃣ Convert plaintext into 8-bit binary  
    2️⃣ Apply Initial Permutation (IP)  
    3️⃣ Perform two Feistel rounds:  
       - Expand R to 8-bits (EP)  
       - XOR with round key  
       - Pass through S-boxes  
       - Apply P4 permutation  
       - XOR with L (Swap L & R)  
    4️⃣ Apply Final Permutation (FP) to get ciphertext  


7️⃣ Vernam Cipher (One-Time Pad)  📂 Path: ciphers/Vernam.py
    
    1️⃣ Convert plaintext and key to binary  
    2️⃣ XOR plaintext binary with key binary  
    3️⃣ Convert back to text for ciphertext  

8️⃣ Vigenère Cipher  📂 Path: ciphers/Vigenere.py
    
    1️⃣ Repeat the key to match the length of plaintext  
    2️⃣ Convert characters to numeric values (A=0, B=1, ... Z=25)  
    3️⃣ Encrypt using formula: Cipher = (Plain + Key) mod 26  
    4️⃣ Convert back to letters for ciphertext  

🏗️ Client-Server also implemented so can run all in terminal
first run server.py in one terminal and 
then run client.py in another terminal ...
