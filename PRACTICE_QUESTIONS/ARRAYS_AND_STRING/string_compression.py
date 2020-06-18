text = input("Enter the text to compress: \n")


def compress_string(text):
    compressed = ""
    current = text[0]
    current_count = 1

    for i, new in enumerate(text):
        if i == 0: continue
        if current == new:
            current_count += 1
        else:
            compressed += current + str(current_count)
            current = new
            current_count = 1
    compressed += current + str(current_count)
    return compressed



print("\n compressed string is :", compress_string(text))
