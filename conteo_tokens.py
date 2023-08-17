import tiktoken

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))

    return num_tokens, [encoding.decode_single_token_bytes(token).decode('utf-8', 'ignore')
                        for token in encoding.encode(string)]

def main():
    texto = input("Ingresa texto para contar tokens:\n")
    print(num_tokens_from_string(texto))

if __name__ == '__main__':
    main()
