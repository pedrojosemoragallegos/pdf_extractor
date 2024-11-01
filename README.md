# PDF Table Extractor

This project provides an executable tool for extracting tables from a PDF file and saving them as CSV files. The script is bundled into an executable file (`pdf_table_extractor.exe`) so you can run it on Windows without needing to install Python or any dependencies.

## Features

- Extracts tables from each page of a PDF file.
- Saves each table as a separate CSV file.
- Displays progress in the console with a progress bar.

## Requirements

- Windows OS (tested with Windows 10/11)
- PowerShell or Command Prompt to run the executable

## Installation

1. **Download the Executable**: Copy or download the executable file `pdf_table_extractor.exe` to a folder on your machine.

## Usage

### Basic Command

To run the executable, open a terminal (PowerShell or Command Prompt), navigate to the directory containing `pdf_table_extractor.exe`, and use the following command format:

```powershell
.\pdf_table_extractor.exe <pdf_path> <output_dir>
