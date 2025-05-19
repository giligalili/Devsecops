import string
import random

def make_enc_key():
    """יוצר מפתח הצפנה כצופן החלפה"""
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    shuffled_letters = letters[:]
    random.shuffle(shuffled_letters)
    encryption_key = dict(zip(letters, shuffled_letters))
    return encryption_key

def compute_dec_key(enc_key):
    """יוצר מפתח פענוח מצופן החלפה"""
    decryption_key = {v: k for k, v in enc_key.items()}
    return decryption_key

# יצירת מפתח הצפנה
enc_key = make_enc_key()

# יצירת מפתח פענוח
dec_key = compute_dec_key(enc_key)

def encrypt_text(free_text, enc_key):
    """מצפין טקסט לפי מפתח הצפנה"""
    out_text = ""

    for char in free_text:
        out_text += enc_key.get(char, char)  # החלפה לפי מפתח, אם התו אינו קיים משאירים אותו כמות שהוא

    print(out_text)
    return out_text

def decrypt_text(out_text, dec_key):
    """מפענח טקסט לפי מפתח פיענוח"""
    in_text = ""

    for char in out_text:
        in_text += dec_key.get(char, char)  # החלפה לפי מפתח, אם התו אינו קיים משאירים אותו כמות שהוא
    return in_text

def test_all(user_text):
    user_text = input("Enter Text To Encrypt:")
    encrypted_text = encrypt_text(user_text, enc_key)
    decryption_text = decrypt_text(encrypted_text, dec_key)
    print("Encrypted_Text:", encrypted_text)
    print("Decryption_Text:", decryption_text)








