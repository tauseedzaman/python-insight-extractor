# Python Insight Extractor

This Python project uses the SpaCy library to extract named entities from a given text file. The extracted entities are categorized by their types (such as `PERSON`, `ORG`, `GPE`, etc.) and stored in separate text files. 

## Features
- Extracts named entities from a `.txt` file.
- Categorizes entities by their labels (such as `PERSON`, `ORG`, `DATE`, etc.).
- Saves each category of entities in a separate text file inside the `output/` folder.

## Requirements

- Python 3.6 or above
- SpaCy
- SpaCy's `en_core_web_md` model

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/tauseedzaman/python-insight-extractor.git
    cd python-insight-extractor
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the SpaCy language model:
    ```bash
    python -m spacy download en_core_web_md
    ```

## Usage

1. Prepare a text file you want to analyze. Ensure the file is in `.txt` format.

2. Run the script:
    ```bash
    python script.py
    ```

3. When prompted, enter the path to your `.txt` file.

4. The script will analyze the text and save the extracted entities to the `output/` directory, with each file corresponding to an entity label (e.g., `PERSON.txt`, `ORG.txt`, etc.).

### Example

If you provide a text file with the following content:
```
Elon Musk is the CEO of SpaceX, which is based in California.
```

The script will create two files:
- `PERSON.txt` containing `Elon Musk`
- `ORG.txt` containing `SpaceX`
- `GPE.txt` containing `California`

## Handling Errors

If the input file is not found, the script will notify you with:
```
File not found. Please check the path and try again.
```

If an invalid file type is provided (non `.txt`), the script will repeatedly prompt for a valid `.txt` file.

## Running the Script in Jupyter Notebook

You can also run this script in a Jupyter Notebook. Simply load the notebook and modify the input file path directly in the notebook cells, then execute the code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to adjust or expand any sections based on the specifics of your project!