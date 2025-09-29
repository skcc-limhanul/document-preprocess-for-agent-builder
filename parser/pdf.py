import pdfplumber

def parse_content(file_path):
    '''
    Extracts plain text and tables from a PDF file.
    
    Parameters:
    * file_path : The path to the PDF file
    
    Returns:
    * parsed_text : Parsed contents including plain text and markdown-style tables
    '''
    output = ''
    previous_table_header = None
    current_table = []
    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                output += '\n' + text.strip() + '\n'
            tables = page.extract_tables()
            for table in tables:
                if not table or not any(table):
                    continue
                header = [cell if isinstance(cell, str) else '' for cell in table[0]]
                rows = table[1:]

                if previous_table_header == header:
                    current_table.extend(rows)
                else:
                    if current_table and previous_table_header:
                        output += '\n'
                        output += '| ' + ' | '.join(cell if isinstance(cell, str) else '' for cell in previous_table_header) + ' |\n'
                        output += '| ' + ' | '.join(['---'] * len(previous_table_header)) + ' |\n'
                        for row in current_table:
                            output += '| ' + ' | '.join(cell.strip() if isinstance(cell, str) else '' for cell in row) + ' |\n'
                    previous_table_header = header
                    current_table = rows
        if current_table and previous_table_header:
            output += '\n'
            output += '| ' + ' | '.join(cell if isinstance(cell, str) else '' for cell in previous_table_header) + ' |\n'
            output += '| ' + ' | '.join(['---'] * len(previous_table_header)) + ' |\n'
            for row in current_table:
                output += '| ' + ' | '.join(cell.strip() if isinstance(cell, str) else '' for cell in row) + ' |\n'
    return output
