from parser import docx, pdf, pptx, xlsx, export
import os
import math

# Variables
file_name_to_export = 'documents_skbp'
input_path = 'c:/temporary_documents/input/' # Path of input documents directory
input_path = 'c:/Users/Administrator/Downloads/1/' # Path of input documents directory
output_path = 'c:/temporary_documents/output/' # Path of output documents directory
output_path = 'c:/Users/Administrator/Downloads/1/' # Path of output documents directory
max_output = 10  # Number of output documents for instant agent builder

# Create documents list to parse merged documents
file_total = os.listdir(input_path)
max_doc = math.ceil(len(file_total) / max_output)
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
        document_title = file_name[::-1][file_name[::-1].find('.')+1:][::-1]
        file_path = f'{input_path}/{file_name}'
        for _func_parser in [docx.parse_content, pdf.parse_content, pptx.parse_content, xlsx.parse_content]:
            try:
                document_text = _func_parser(file_path)
                # documents_merged = documents_merged + '\n\n' + document_text
                documents_merged = f"{documents_merged}\n\n###문서제목 : {document_title}\n{document_text}"
                documents_merged = documents_merged.strip()
                print(f"Done : {file_path}")
                break
            except Exception as e:
                print(f"\nFailed: {file_path}\n{e}\n")
    documents_merged = documents_merged.strip()
    export.to_pdf_portrait(documents_merged, f'{output_path}/doc_portrait_{ix:002}.pdf')
    # export.to_pdf_landscape(documents_merged, f'{output_path}/doc_landscape_{ix:002}.pdf')

    # with open(f'{output_path}/{file_name_to_export}_{ix}.txt', 'w', encoding='utf-8') as io_file:
    #     io_file.write(documents_merged)
