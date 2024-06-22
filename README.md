
# PDF Analyzer

PDF Analyzer is a tool to extract and analyze repeatedly asked questions from PDF files.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/psycho-prince/pdf_analyzer.git
    cd pdf_analyzer
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To analyze questions in one or more PDF files, run:
```sh
python pdf_analyzer.py file1.pdf file2.pdf file3.pdf
