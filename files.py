

def main():
    with open('input_data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            content = f.read()
            print(content)
    # with open('referat2.txt', 'w', encoding='utf-8') as referat_2:
    #      referat_2.write(content)


if __name__ == "__main__":
    main()
