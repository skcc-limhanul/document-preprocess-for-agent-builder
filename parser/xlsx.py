from openpyxl import load_workbook


def parse_content(file_path):
    '''
    Extract contents from xlsx including merged cells, collapsing them to show only the first value.
    Parameter:
    * file_path : The path to xlsx
    Return:
    * parsed_text : Parsed contents like plain texts and markdown style tables
    '''
    parsed_text = ''
    wb = load_workbook(file_path, data_only=True)
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        parsed_text += f"\n### Sheet: {sheet_name}\n\n"

        merged_cell_map = {}
        for merged_range in ws.merged_cells.ranges:
            min_row, min_col = merged_range.min_row, merged_range.min_col
            value = ws.cell(row=min_row, column=min_col).value
            for row in ws.iter_rows(min_row=merged_range.min_row, max_row=merged_range.max_row,
                                    min_col=merged_range.min_col, max_col=merged_range.max_col):
                for cell in row:
                    merged_cell_map[(cell.row, cell.column)] = value

        for row in ws.iter_rows():
            row_text = []
            for cell in row:
                val = cell.value
                if val is None and (cell.row, cell.column) in merged_cell_map:
                    val = merged_cell_map[(cell.row, cell.column)]
                row_text.append(str(val).strip() if val else '')
            
            if all(cell == '' for cell in row_text):
                parsed_text += '\n'
                continue

            non_empty_count = sum(1 for cell in row_text if cell != '')
            if non_empty_count >= 3:
                parsed_text += '| ' + ' | '.join(row_text) + ' |\n'
            else:
                parsed_text += ' '.join(row_text) + '\n'
    return parsed_text
