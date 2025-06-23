# XML_Converter
This project provides a lightweight desktop tool for converting structured text data into an XML format, using predefined XML templates. It is built with Python and a simple Tkinter-based GUI for ease of use.
Features
Reads structured data from a text file

Parses key-value pairs and invoice lines

Fills in two XML templates (index.xml and invoiceLine.xml) using the data

Outputs a complete XML file ready for use

Simple graphical interface for selecting input and output files

Files
conversion_algorithm.py
Contains the core logic:

find_word(file_path): Parses key-value pairs from the input text file.

invoice_line(...): Fills invoice line XML template with provided data.

read_table(file_path): Extracts the table section from the input file.

select_data_from_chunks(string): Converts table lines into multiple invoice line XML blocks.

convert_file(file_to_convert, destination): Merges all components into a final XML file.

main.py
A simple GUI built using tkinter

Lets the user select the source file and output destination

Triggers the conversion process on button click

Requirements
Python 3.6+

No external libraries required (only tkinter, which comes with Python standard library)

Usage
Make sure your project directory contains:

assets/index.xml

assets/invoiceLine.xml

Run main.py.

Enter the full path to the file you want to convert.

Enter the destination path for the output file.

Click "Convert".

The output XML will be saved to the specified location.

Notes
The format of the input text file must match the expected structure for proper parsing.

The XML templates must contain placeholders such as object_date_creation, id, name, tax, etc., to be replaced during conversion.
