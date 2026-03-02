import pdfplumber
import pandas as pd


def pdf_to_csv(pdf_path, output_csv):

    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            tables = page.extract_tables()

            for table in tables:
                df = pd.DataFrame(table)
                all_tables.append(df)

    final_df = pd.concat(all_tables, ignore_index=True)

    final_df.to_csv(output_csv, index=False)

    return final_df