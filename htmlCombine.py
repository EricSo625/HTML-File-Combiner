from bs4 import BeautifulSoup, Tag
import os
import tkinter as tk
from tkinter import filedialog

def combine_html_files(dir_path, output_file_name):
    html_files = [f for f in os.listdir(dir_path) if f.endswith(".html")]

    # Create a new BeautifulSoup object
    soup = BeautifulSoup("", 'lxml')

    # Create a <body> tag if it doesn't exist
    if soup.body is None:
        body = Tag(builder=soup.builder, name="body")
        soup.append(body)

    # Loop through the HTML files and combine them
    for html_file in html_files:
        try:
            with open(os.path.join(dir_path, html_file), 'r', encoding='utf-8') as f:
                file_soup = BeautifulSoup(f, 'lxml')
        except UnicodeDecodeError:
            try:
                with open(os.path.join(dir_path, html_file), 'r', encoding='big5') as f:
                    file_soup = BeautifulSoup(f, 'lxml')
            except UnicodeDecodeError:
                print(f'Could not decode file {html_file} with UTF-8 or Big5 encoding.')
                continue

        # Append the body of the file to the soup object
        soup.body.append(file_soup.body)

    # Write the combined HTML to a new file
    with open(os.path.join(dir_path, output_file_name), 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))

def main():
    # Create a root TK window (and immediately hide it)
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to select a directory
    dir_path = filedialog.askdirectory()

    # Prompt the user to select a name for the output file
    output_file_name = filedialog.asksaveasfilename(defaultextension=".html")

    # Combine the HTML files
    combine_html_files(dir_path, output_file_name)

# Run the main function
if __name__ == "__main__":
    main()