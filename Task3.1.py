class IndexAlreadyTaken(Exception):
    pass

def hashing_method(value_to_hash, memory):
    hashed_value = 0
    for char in value_to_hash:
        hashed_value += ord(char)

    index_val = int(hashed_value % 30)

    if memory[index_val] is None:
        memory[index_val] = value_to_hash
    else:
        raise IndexAlreadyTaken(f"Your index {index_val} is already taken.")
    print(f"Your hashed key is at index: {index_val}")
    print(memory)

memory = [None] * 30

while True:
    print("Hash Keys Simulator - 'exit' to Exit")
    value = input("Give me a key to hash: ")

    if value.lower() == 'exit':
        break

    try:
        hashing_method(value, memory)
    except IndexAlreadyTaken as e:
        print(e)

    print("\n\n")
