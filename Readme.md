# auto-DRE

**auto-DRE** is a small Python application designed to *automate* part of the *financial reporting process* for a small business.  
It asks for a daily financial control file, adds month information, reads data from it and updates an income statement.

This project was developed for a dental clinic to optimize its internal *financial management*. I received **full authorization** to publish it on GitHub as part of my professional portfolio, demonstrating the use of Python for real-world *automation* in a business context.

At the end of this document, I describe how to run **auto-DRE** with some sample files included in this repository.

---

## Features

- Reads daily expense and revenue data from Excel files.
- Adds the current month to the proper columns through user input.
- Merges new data from the daily financial control file into an existing income statement file.
- Replaces old sheets with updated ones to keep reports consistent.
- Displays the resulting data shapes for quick validation.

---

## File Overview

| File | Description |
|------|--------------|
| *auto_dre.py* | Adds the selected month to the "RESUMO DESPESAS" and "RESUMO RECEITAS" sheets in the daily report file. |
| *feeder.py* | Combines the daily report with the master DRE spreadsheet and updates its data. |

---

## How It Works

1. The user runs `auto_dre.py` and enters:
   - The name of the daily financial report file (`file.extension`)
   - The month to be recorded

   The script updates the month column in both the expense and revenue sheets.

2. The user then runs `feeder.py`, which:
   - Reads data from both the daily financial control and the DRE file  
   - Concatenates new data  
   - Writes the updated tables back to the DRE file  

3. The console prints the shape of the resulting data for quick checks.

---

## Requirements

- Python 3.9+
- pandas
- openpyxl

To install the dependencies:
   ```bash
   pip install pandas openpyxl
   ```

---

## Example Usage

   ```bash
   python auto_dre.py
   # Enter the file name: CONTROLE DIÁRIO - teste.xlsx
   # Enter the month: March
   ```
   ```bash
   python feeder.py
   ```

After execution, the DRE file is automatically updated with the new data.

---

## Sample Data

To make testing easier, this repository includes sample Excel files that simulate the real financial data from the dental clinic.
They can be used to test the scripts without any additional setup.

### File	Overview

| File | Description |
|------|--------------|
| *Controle Diário.xlsx* | Example of a daily financial control report with expenses and revenues. |
| *DRE - DEMONSTRATIVO DE RESULTADO.xlsx* | Example of a DRE file used as the income statement. |

You can run the scripts directly using these files to reproduce the app’s workflow.


