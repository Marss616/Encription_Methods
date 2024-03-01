import hashlib

def my_hash(data):
    # Convert data to bytes if needed
    if not isinstance(data, bytes):
        data = str(data).encode()

    # Create a hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the data
    hash_object.update(data)

    # Get the hexadecimal representation of the hash
    hash_value = hash_object.hexdigest()

    return hash_value # Return the hash value

# Example usage
data = "Hello, World!"
hashed_data = my_hash(data)
print(hashed_data)