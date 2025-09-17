from docx import Document
from lxml import etree
import re


def _clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)
    return text.strip()


def parse_content(file_path):
    '''
    Extracts plain text and tables from a MS Word file.
    Parameters:
    * file_path : The path to docx
    Returns:
    * parsed_text : Parsed contents like plain texts and markdown style tables
    '''
    parsed_text = ''
    doc = Document(file_path)
    main_document_part = doc.part

    tree = etree.XML(main_document_part.blob)
    nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    for elem in tree.iter():
        tag = etree.QName(elem).localname

        if tag == 'p':
            texts = [node.text for node in elem.xpath('.//w:t', namespaces=nsmap) if node.text]
            if texts:
                raw_text = ' '.join(texts)
                parsed_text = parsed_text + '\n' + _clean_text(raw_text)

        elif tag == 'tbl':
            rows = elem.xpath('.//w:tr', namespaces=nsmap)
            if not rows:
                continue

            table_data = []
            for row in rows:
                cells = row.xpath('.//w:tc', namespaces=nsmap)
                row_text = []
                for cell in cells:
                    cell_texts = [t.text for t in cell.xpath('.//w:t', namespaces=nsmap) if t.text]
                    row_text.append(_clean_text(' '.join(cell_texts)))
                table_data.append(row_text)

            if table_data:
                header = table_data[0]
                parsed_text = parsed_text + '\n' + '| ' + ' | '.join(header) + ' |'
                parsed_text = parsed_text + '\n' + '| ' + ' | '.join(['---'] * len(header)) + ' |'
                for row in table_data[1:]:
                    parsed_text = parsed_text + '\n' + '| ' + ' | '.join(row) + ' |'
    return parsed_text.strip()
