#! /usr/bin/env python3
# pdf_paranoia - Walks through a directory and encrypts pdf files.

import PyPDF2
import os
import pyinputplus
from pathlib import Path

## Prompt user for a directory to search
## Prompt user for encryption password
##  Use os.walk() and grab all PDF files ## Using pathlib.Path.rglob() seemed more efficient
## Encrypt the PDFs and rename them with {name}_encrypted.pdf
## Prompt user if they want to delete the original files and execute selection action


def prompt_file_path():
    file_path = pyinputplus.inputFilepath(prompt="Enter a directory to search:\n")
    file_path = Path(file_path).absolute()
    if Path(file_path).exists() == False:
        print("Please enter an existing directory...")
        prompt_file_path()
    return file_path


def prompt_encryption_key():
    password = pyinputplus.inputPassword(
        prompt="Enter a password to use as the encryption key:\n"
    )
    return password


def grab_pdfs(file_path):
    glob_obj = Path(file_path).rglob("*.pdf")
    pdf_files = [file for file in list(glob_obj)]
    return pdf_files


def encrypt_pdfs(pdf_files, password):
    for file in pdf_files:
        pdf_file = open(file, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        pdf_writer.encrypt(password)
        encrypted_pdf = open(
            f"{Path.joinpath(file.parent, file.name.replace('.pdf', '_encrypted.pdf'))}",
            "wb",
        )
        pdf_writer.write(encrypted_pdf)
        encrypted_pdf.close()


def test(file_path, password):
    glob_obj = Path(file_path).rglob(r"*_encrypted.pdf")
    pdf_files = [file for file in list(glob_obj)]
    for file in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(open(file, "rb"))
        if pdf_reader.isEncrypted & pdf_reader.decrypt(password):
            return True
        else:
            return False


def delete_originals(pdf_files):
    for file in pdf_files:
        os.remove(file)


def main():
    print("pdf_paranoia_0.0.1")
    print("pdf_paranoia will encrypt your PDF files.")
    file_path = prompt_file_path()
    password = prompt_encryption_key()
    pdf_files = grab_pdfs(file_path)
    if pdf_files == []:
        print("No PDF files were found in the given directory.")
        return None
    encrypt_pdfs(pdf_files, password)
    if test(file_path, password):
        print(f"All PDF files in {file_path} were properly encrypted.")
    else:
        print(f"PDF files in {file_path} were not properly encrypted.")
        return None
    response = pyinputplus.inputYesNo(
        prompt="Would you like to delete the original, unecrypted files?\n",
        yesVal="yes",
        noVal="no",
    )
    if response == "no":
        print("pdf_paranoia.py has finished running.")
    elif response == "yes":
        delete_originals(pdf_files)
        print(
            "Unencrypted PDF files have been deleted.  Thank you for using pdf_paranoia."
        )


if __name__ == "__main__":
    main()
