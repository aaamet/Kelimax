import itertools

def start_generator():

    characters = input(" Characters > ")
    min_length = int(input(" Minimum Length > "))
    max_length = int(input(" Maximum Length > "))

    output_file = open("output.txt", "w")

    print(" Processing...")

    for n in range(min_length, max_length+1):
        for xs in itertools.product(characters, repeat=n):
            output_file.write(''.join(map(str, xs)) + "\n")

    print(" Done!")
    output_file.close()
