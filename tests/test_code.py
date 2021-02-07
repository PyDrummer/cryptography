from caesar_cipher.caesar_cipher import encrypt, decrypt, crack

test = "Ravenala"
test2 = 'It was the best of times, it was the worst of times.'
key = 2
key2 = 6

def test_encrypt():
    actual = encrypt(test, key)
    expected = 'Tcxgpcnc'
    assert actual == expected

def test_decrypt():
    tester = encrypt(test, key)
    actual = decrypt(tester, key)
    expected = "Ravenala"
    assert actual == expected

def test_crack():
    crack_test = encrypt(test2, key)
    actual = crack(crack_test)
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected

def test_crack_again():
    crack_test = encrypt(test2, key2)
    actual = crack(crack_test)
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected