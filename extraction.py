import pdfplumber
import pandas as pd

def process_pdf(pdf_path):
    all_text = []
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages: #naviguer sur les pages du pdf

            # Extraire les tables
            for table in page.find_tables(): #naviguer sur les tables de chaque page
                data = table.extract()

                if data:
                    #stocker la data dans un data frame
                    df = pd.DataFrame(data[1:], columns=data[0]) # data[0] is the row of columns and data[1:] are the rows of data
                    #convertir le data frame en markdown
                    markdown = df.to_markdown(index=False)
                    all_tables.append(markdown)

            # Extraire le texte de la page (sans tables)
            text = page.extract_text()

            if text:
                all_text.append(text)

    return "\n".join(all_text), "\n".join(all_tables)


#  Execution
# pdf_path = r"C:\Users\Pc\Desktop\Cours IoT_Partie I - Pr Boudlal.pdf"
# # text, tables = process_pdf(pdf_path)

# print("TEXT:\n", text)
# print("\nTABLES:\n", tables)