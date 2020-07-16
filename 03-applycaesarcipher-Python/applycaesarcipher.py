# A Caesar Cipher is a simple cipher that works by shifting each letter in
# the given message by a certain number. For example, if we shift the message
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given
# message by shift letters. You are guaranteed that message is a string, and
# that shift is an integer between -25 and 25. Capital letters should stay capital
# and lowercase letters should stay lowercase, and non-letter characters should not be changed.
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
    result = ""
    for ch in msg:
        capital = False
        if ch.isupper():
            capital = True
            ch = ch.lower()
        if 97 <= ord(ch) <= 122:
            if ord(ch) + shift > 122:
                if capital:
                    result += (chr(96 + ord(ch) + shift - 122)).upper()
                else:
                    result += chr(96 + ord(ch) + shift - 122)
            elif ord(ch) + shift < 97:
                if capital:
                    result += (chr(123 - (97 - (ord(ch) + shift)))).upper()
                else:
                    result += chr(123 - (97 - (ord(ch) + shift)))
            else:
                if capital:
                    result += (chr(ord(ch) + shift)).upper()
                else:
                    result += chr(ord(ch) + shift)
        else:
            result += ch
    return result
