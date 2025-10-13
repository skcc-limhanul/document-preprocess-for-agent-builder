import os
import math
from pathlib import Path

from parser import docx, pdf, pptx, xlsx

# Variables
file_name_to_export = 'documents_skmr'
input_path = 'documents'  # Path of input documents directory
output_path = 'parsed'  # Path of output documents directory
max_output = 10  # Number of output documents for instant agent builder


def pick_parser(file_path):
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        # 시그니처도 확인
        with open(file_path, "rb") as f:
            head = f.read(5)
        if head.startswith(b"%PDF-"):
            return pdf.parse_content
        else:
            raise ValueError("파일 확장자는 .pdf지만 PDF 시그니처가 아닙니다.")
    elif ext == ".docx":
        return docx.parse_content
    elif ext == ".pptx":
        return pptx.parse_content
    elif ext == ".xlsx":
        return xlsx.parse_content
    else:
        raise ValueError(f"지원하지 않는 확장자: {ext}")


def parse_any(file_path):
    parser = pick_parser(file_path)
    return parser(file_path)


def main():
    # Create documents list to parse merged documents
    try:
        file_total = os.listdir(input_path)
    except:
        print(f"No such file or directory: '{input_path}'")
        return

    if len(file_total) == 0:
        print(f"No files in the input path: '{input_path}'")
        return

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
            # file_path = f'{input_path}/{file_name}'   # 윈도우용??
            file_path = os.path.join(os.getcwd(), input_path, file_name)
            try:
                document_text = parse_any(file_path)
                documents_merged = documents_merged + '\n\n' + document_text
                print(f"Done : {file_path}")
                break
            except Exception as e:
                print(f"\nFailed: {file_path}\n{e}\n")

        documents_merged = documents_merged.strip()

        with open(f'{output_path}/{file_name_to_export}_{ix}.txt', 'w', encoding='utf-8') as io_file:
            io_file.write(documents_merged)


if __name__ == "__main__":
    main()
