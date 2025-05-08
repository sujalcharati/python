def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Extended Euclidean Algorithm to find modular inverse
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(cipher, d, n):
    return pow(cipher, d, n)

# Step 1: Choose two prime numbers
p = 61
q = 53

# Step 2: Compute n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e
e = 17  # should be coprime with phi

# Step 4: Compute d (modular inverse of e mod phi)
d = mod_inverse(e, phi)

# Display the keys
print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")

# Step 5: Encrypt a message
message = 123  # any integer < n
cipher = encrypt(message, e, n)
print(f"Encrypted message: {cipher}")

# Step 6: Decrypt the message
decrypted = decrypt(cipher, d, n)
print(f"Decrypted message: {decrypted}")
