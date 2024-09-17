import spacy

# Load the Spacy model
nlp = spacy.load("en_core_web_md")

def extract_entities(input_file):
    # Open the input file
    try:
        with open(input_file, 'r', encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return

    # Extract entities
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)

    # Store entities in separate files
    for label, ent_list in entities.items():
        with open(f"output/{label}.txt", 'w', encoding="utf-8") as f:
            for ent in set(ent_list):
                f.write(ent + "\n")

# Ask user for input file path
input_file = input("Please enter the input text file path: ")

# Validate input file path
while not input_file.endswith(".txt"):
    print("Invalid file type. Please enter a .txt file path.")
    input_file = input("Please enter the input text file path: ")

# Call the function
extract_entities(input_file)