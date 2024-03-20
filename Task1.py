'''The encryption and decryption in python project requires you to implement a transposition cipher classs incorporating the following elements: A constructor function that accepts the cipher's key as an argument. A method designated for encyrpting a message requiring a single parameter-the plain text message to be encrypted'''
class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self,p):
        c=len(self.key)
        r=(len(p)+c-1)//c
        padded=p.ljust(r*c)
        grid = [['' for _ in range(c)] for _ in range(r)]
        for i, char in enumerate(padded):
            row=i//c
            col=i%c
            grid[row][col]=char
        encrypted_columns=['']*c
        for col_index, key_value in enumerate(self.key):
            for row_index in range(r):
                encrypted_columns[col_index] += grid[row_index][int(key_value) - 1]
        encrypted_message = ''.join(encrypted_columns)
        return encrypted_message
cipher = TranspositionCipher("4321")
p=input("Enter the text to encrypt")
encrypted_text = cipher.encrypt(p)
print("\nEncrypted message:", encrypted_text)
