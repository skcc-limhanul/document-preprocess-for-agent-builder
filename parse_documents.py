from parser import docx, pdf, pptx, xlsx
import os


# Variables
dir_path = 'c:/temporary_documents/' # Path of input documents directory
max_doc = 30  # Number of input documents which merged to one output document

# Create documents list to parse merged documents
file_total = os.listdir(dir_path)
file_list = []
ix = 0
while len(file_total) > 0:
    file_part = file_total[ix*max_doc:(ix+1)*max_doc]
    if len(file_part) != 0:
        file_list.append(file_part)
    else:
        break
    ix += 1

# Parse documents (export to txt format)
for ix, file_names in enumerate(file_list, start=1):
    documents_merged = ''
    for file_name in file_names:
        file_path = f'{dir_path}{file_name}'
        for _func_parser in [docx.parse_content, pdf.parse_content, pptx.parse_content, xlsx.parse_content]:
            try:
                document_text = _func_parser(file_path)
                documents_merged = documents_merged + '\n' + document_text
                print(f"Done : {file_path}")
                break
            except Exception as e:
                print(f"\nFailed: {file_path}\n{e}\n")
    documents_merged = documents_merged.strip()

    with open(f'documents_skbp_{ix}.txt', 'w', encoding='utf-8') as io_file:
        io_file.write(documents_merged)
