import argparse
import PyPDF2
import re
import nltk
from collections import Counter

nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extract_text()
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n', ' ', text)
    return text

def preprocess_text(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def find_questions(sentences):
    questions = [sentence for sentence in sentences if sentence.endswith('?')]
    return questions

def analyze_frequency(questions):
    counter = Counter(questions)
    most_common_questions = counter.most_common()
    return most_common_questions

def main(pdf_paths):
    all_questions = []
    for pdf_path in pdf_paths:
        text = extract_text_from_pdf(pdf_path)
        clean = clean_text(text)
        sentences = preprocess_text(clean)
        questions = find_questions(sentences)
        all_questions.extend(questions)

    most_common_questions = analyze_frequency(all_questions)
    for question, frequency in most_common_questions:
        print(f"{question}: {frequency} times")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process PDFs and find frequently asked questions.')
    parser.add_argument('pdf_paths', metavar='N', type=str, nargs='+', help='paths to the PDF files')
    args = parser.parse_args()
    main(args.pdf_paths)
