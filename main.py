# START

import textwrap

# encrypts text using Rail Fence pattern
def encrypt_rail_fence(text,num_rails) :

    rails=['' for _ in range(num_rails)]
    rail=0
    direction=1

    for char in text :
        rails[rail]+=char
        rail+=direction
        if rail==0 or rail==num_rails-1:
            direction*=-1

    return ''.join(rails)


# decrypts text using Rail Fence pattern
def decrypt_rail_fence(cipher,num_rails) : 
    grid=[['' for _ in range(len(cipher))] for _ in range(num_rails)]

    rail=0
    direction=1
    for a in range(len(cipher)) :
        grid[rail][a]='*'
        rail+=direction
        if rail==0 or rail==num_rails-1:
            direction*=-1

    idx=0
    for r in range(num_rails) :
        for c in range(len(cipher)):
            if grid[r][c]=='*' and idx<len(cipher):
                grid[r][c]=cipher[idx]
                idx += 1

    decrypted = ''
    rail=0
    direction=1
    for a in range(len(cipher)):
        decrypted+=grid[rail][a]
        rail+=direction
        if rail==0 or rail==num_rails-1:
            direction*=-1

    return decrypted

# groups text into chunks for readability
def format_output(text,group_size=5):
    return ' '.join(textwrap.wrap(text,group_size))

# extracts cleaned characters , space positions , and case flags
def process_text(text) : 
    cleaned=[]
    spaces=[]
    casing=[]

    for a,char in enumerate(text) :
        if char == ' ':
            spaces.append(a)
        elif char.isalpha() :
            cleaned.append(char.lower())
            casing.append(char.isupper())

    return ''.join(cleaned),spaces,casing


# re-applies original casing and spaces
def restore_text(text,spaces,casing) :
    final=''.join(c.upper() if casing[a] else c for a, c in enumerate(text))
    for pos in spaces :
        if pos<len(final) :
            final=final[:pos] + ' ' + final[pos:]
        else:
            final+=' '
    return final

def main() :
    while True:
        print("\n========= Rail Fence Cipher ========")
        print("1 . Encrypt")
        print("2 . Decrypt")
        print("3 . Exit")

        option=input("Enter choice (1/2/3) : ").strip()

        if option=='1' :
            original=input("Enter plain text : ").strip()
            if not original :
                print("Error !!! : Empty input.")
                continue

            try :
                rails=int(input("Enter number of rails (minimun 2) : "))
            except ValueError :
                print("Error !!! : Invalid number.")
                continue

            clean,spaces,case_flags=process_text(original)

            if rails<2 :
                print("Error !!! : At least 2 rails required.")
                continue 
            elif rails>len(clean) :
                print("Warning !!! : Rails exceed message length.")

            cipher=encrypt_rail_fence(clean,rails)
            output=restore_text(cipher,spaces,case_flags)
            print("Encrypted Text : ",format_output(output))

        elif option=='2' :
            cipher_input=input("Enter cipher text : ").strip()
            if not cipher_input :
                print("Error !!! : Empty input.")
                continue

            try:
                rails=int(input("Enter number of rails (minimum 2) : "))
            except ValueError :
                print("Error !!! : Invalid number.")
                continue

            clean,spaces,case_flags=process_text(cipher_input)

            if rails<2 :
                print("Error !!! : At least 2 rails required.")
                continue
            elif rails>len(clean):
                print("Warning !!! : Rails exceed cipher length.")

            plain=decrypt_rail_fence(clean,rails)
            output=restore_text(plain,spaces,case_flags)
            print("Decrypted Text : ",format_output(output))

        elif option=='3' :
            print("Goodbye!   :)")
            break

        else:
            print("Invalid option. Please choose 1 , 2 , or 3.")

main()

# END
