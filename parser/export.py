from fpdf import FPDF

# def to_pdf(input_text, output_path, title_header_og="###문서제목", title_header_nw="# 문서제목", font_path="c:/Windows/Fonts/malgun.ttf"):
#     '''
#     Export plain text to PDF.
    
#     Parameters:
#     * input_text : Plain text
#     * output_path : File path of PDF to export
#     * title_header_og : 
    
#     Returns:
#     * parsed_text : Parsed contents including plain text and markdown-style tables
#     '''
#     try:
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.add_font("KoreanFont", fname=font_path, uni=True)

#         normal_font_size = 9
#         title_font_size = 14

#         pdf.set_font("KoreanFont", size=normal_font_size)
        
#         for line in input_text.split('\n'):
#             line = line.strip()
#             if line.startswith(title_header_og):
#                 pdf.set_font("KoreanFont", size=title_font_size)
#                 title_text = line.replace(title_header_og, title_header_nw).strip()
#                 pdf.cell(0, 10, title_text, ln=True)
#                 pdf.set_font("KoreanFont", size=normal_font_size)
#             elif line:
#                 pdf.multi_cell(0, 8, line)
#             else:
#                 pdf.ln(8)
        
#         pdf.output(output_path)
#     except Exception as e:
#         print(f"** Error *******************************)\n****************************************\n{e}")


# def to_pdf(input_text, output_path, title_header_og="###문서제목", title_header_nw="# 문서제목", font_path="c:/Windows/Fonts/malgun.ttf"):
#     '''
#     Export plain text with Markdown-style tables to PDF.
    
#     Parameters:
#     * input_text : Plain text
#     * output_path : File path of PDF to export
#     '''
#     try:
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.add_font("KoreanFont", fname=font_path, uni=True)

#         normal_font_size = 9
#         title_font_size = 14
#         line_height = 8
#         col_width = 40  # You can dynamically calculate based on content if needed

#         pdf.set_font("KoreanFont", size=normal_font_size)

#         lines = input_text.split('\n')
#         i = 0
#         while i < len(lines):
#             line = lines[i].strip()

#             # Title header
#             if line.startswith(title_header_og):
#                 pdf.set_font("KoreanFont", size=title_font_size)
#                 title_text = line.replace(title_header_og, title_header_nw).strip()
#                 pdf.cell(0, 10, title_text, ln=True)
#                 pdf.set_font("KoreanFont", size=normal_font_size)
#                 i += 1
#                 continue

#             # Detect markdown table
#             if "|" in line:
#                 # Look ahead to check for table separator (like |---|---|---|)
#                 if i + 1 < len(lines) and set(lines[i + 1].strip()) <= set("|:- "):
#                     # Begin collecting table rows
#                     table_lines = []
#                     table_lines.append(line)
#                     i += 1
#                     while i < len(lines) and "|" in lines[i]:
#                         table_lines.append(lines[i].strip())
#                         i += 1

#                     # Skip if table doesn't have at least header and one row
#                     if len(table_lines) < 2:
#                         continue

#                     # Parse the table rows (skip the separator)
#                     headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
#                     rows = []
#                     for row_line in table_lines[2:]:  # skip header and separator
#                         row = [cell.strip() for cell in row_line.split("|") if cell.strip()]
#                         if row:
#                             rows.append(row)

#                     # Render header
#                     for header in headers:
#                         pdf.cell(col_width, line_height, txt=header, border=1)
#                     pdf.ln(line_height)

#                     # Render rows
#                     for row in rows:
#                         for j in range(len(headers)):
#                             cell = row[j] if j < len(row) else ""
#                             pdf.cell(col_width, line_height, txt=cell, border=1)
#                         pdf.ln(line_height)
                    
#                     pdf.ln(line_height)  # spacing after table
#                     continue  # skip the default line handling

#             # Normal text line
#             if line:
#                 pdf.multi_cell(0, line_height, line)
#             else:
#                 pdf.ln(line_height)
#             i += 1

#         pdf.output(output_path)
#     except Exception as e:
#         print(f"** Error *******************************\n****************************************\n{e}")









# def to_pdf(input_text, output_path, title_header_og="###문서제목", title_header_nw="# 문서제목", font_path="c:/Windows/Fonts/malgun.ttf"):
#     '''
#     Export plain text with Markdown-style tables to PDF with dynamic column width.
#     '''
#     try:
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.add_font("KoreanFont", fname=font_path, uni=True)

#         normal_font_size = 9
#         title_font_size = 14
#         line_height = 8
#         page_width = pdf.w - 2 * pdf.l_margin  # Available width for content

#         pdf.set_font("KoreanFont", size=normal_font_size)

#         lines = input_text.split('\n')
#         i = 0
#         while i < len(lines):
#             line = lines[i].strip()

#             # Title header
#             if line.startswith(title_header_og):
#                 pdf.set_font("KoreanFont", size=title_font_size)
#                 title_text = line.replace(title_header_og, title_header_nw).strip()
#                 pdf.cell(0, 10, title_text, ln=True)
#                 pdf.set_font("KoreanFont", size=normal_font_size)
#                 i += 1
#                 continue

#             # Detect markdown table
#             if "|" in line:
#                 if i + 1 < len(lines) and set(lines[i + 1].strip()) <= set("|:- "):
#                     table_lines = [line]
#                     i += 1
#                     while i < len(lines) and "|" in lines[i]:
#                         table_lines.append(lines[i].strip())
#                         i += 1

#                     if len(table_lines) < 2:
#                         continue

#                     # Parse headers and rows
#                     headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
#                     rows = []
#                     for row_line in table_lines[2:]:
#                         row = [cell.strip() for cell in row_line.split("|") if cell.strip()]
#                         if row:
#                             rows.append(row)

#                     num_cols = len(headers)

#                     # Calculate max string width per column (header + rows)
#                     max_col_widths = [pdf.get_string_width(header) for header in headers]
#                     for row in rows:
#                         for j in range(num_cols):
#                             cell = row[j] if j < len(row) else ""
#                             cell_width = pdf.get_string_width(cell)
#                             if cell_width > max_col_widths[j]:
#                                 max_col_widths[j] = cell_width

#                     # Scale widths to fit within page width
#                     total_width = sum(max_col_widths)
#                     scale = page_width / total_width if total_width > 0 else 1
#                     scaled_col_widths = [w * scale for w in max_col_widths]

#                     # Render header
#                     for j, header in enumerate(headers):
#                         pdf.cell(scaled_col_widths[j], line_height, txt=header, border=1)
#                     pdf.ln(line_height)

#                     # Render rows
#                     for row in rows:
#                         for j in range(num_cols):
#                             cell = row[j] if j < len(row) else ""
#                             pdf.cell(scaled_col_widths[j], line_height, txt=cell, border=1)
#                         pdf.ln(line_height)

#                     pdf.ln(line_height)
#                     continue

#             # Normal text line
#             if line:
#                 pdf.multi_cell(0, line_height, line)
#             else:
#                 pdf.ln(line_height)
#             i += 1

#         pdf.output(output_path)
#     except Exception as e:
#         print(f"** Error *******************************\n****************************************\n{e}")





# def to_pdf_portrait(input_text, output_path, title_header_og="###문서제목", title_header_nw="# 문서제목", font_path="c:/Windows/Fonts/malgun.ttf"):
#     '''
#     Export plain text with Markdown-style tables to PDF with dynamic column width.
#     Supports tables both with and without separator rows.
#     '''
#     try:
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.add_font("KoreanFont", fname=font_path, uni=True)

#         normal_font_size = 7
#         title_font_size = 12
#         line_height = 8
#         page_width = pdf.w - 2 * pdf.l_margin  # Available width for content

#         pdf.set_font("KoreanFont", size=normal_font_size)

#         lines = input_text.split('\n')
#         i = 0
#         while i < len(lines):
#             line = lines[i].strip()

#             # Title header
#             if line.startswith(title_header_og):
#                 pdf.set_font("KoreanFont", size=title_font_size)
#                 title_text = line.replace(title_header_og, title_header_nw).strip()
#                 pdf.cell(0, 10, title_text, ln=True)
#                 pdf.set_font("KoreanFont", size=normal_font_size)
#                 i += 1
#                 continue

#             # Detect markdown table
#             if "|" in line:
#                 # Check if next line is a separator row
#                 has_separator = (i + 1 < len(lines)) and (set(lines[i + 1].strip()) <= set("|:- "))

#                 table_lines = [line]
#                 i += 1

#                 # Collect lines part of the table (starting at i)
#                 while i < len(lines) and "|" in lines[i]:
#                     # If a separator row exists, skip it from data rows
#                     if has_separator and i == (lines.index(line) + 1):
#                         i += 1
#                         continue
#                     table_lines.append(lines[i].strip())
#                     i += 1

#                 # If no rows, continue
#                 if len(table_lines) < 1:
#                     continue

#                 # If separator exists, headers are first line, data starts after second line
#                 # Else headers are first line, data starts second line
#                 if has_separator:
#                     headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
#                     data_rows = table_lines[1:]  # rows after header and separator handled
#                 else:
#                     headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
#                     data_rows = table_lines[1:]

#                 rows = []
#                 for row_line in data_rows:
#                     row = [cell.strip() for cell in row_line.split("|") if cell.strip()]
#                     if row:
#                         rows.append(row)

#                 num_cols = len(headers)

#                 # Calculate max string width per column (header + rows)
#                 max_col_widths = [pdf.get_string_width(header) for header in headers]
#                 for row in rows:
#                     for j in range(num_cols):
#                         cell = row[j] if j < len(row) else ""
#                         cell_width = pdf.get_string_width(cell)
#                         if cell_width > max_col_widths[j]:
#                             max_col_widths[j] = cell_width

#                 # Scale widths to fit within page width
#                 total_width = sum(max_col_widths)
#                 scale = page_width / total_width if total_width > 0 else 1
#                 scaled_col_widths = [w * scale for w in max_col_widths]

#                 # Render header
#                 for j, header in enumerate(headers):
#                     pdf.cell(scaled_col_widths[j], line_height, txt=header, border=1)
#                 pdf.ln(line_height)

#                 # Render rows
#                 for row in rows:
#                     for j in range(num_cols):
#                         cell = row[j] if j < len(row) else ""
#                         pdf.cell(scaled_col_widths[j], line_height, txt=cell, border=1)
#                     pdf.ln(line_height)

#                 pdf.ln(line_height)
#                 continue

#             # Normal text line
#             if line:
#                 pdf.multi_cell(0, line_height, line)
#             else:
#                 pdf.ln(line_height)
#             i += 1

#         pdf.output(output_path)
#     except Exception as e:
#         print(f"** Error *******************************\n****************************************\n{e}")


import math

def to_pdf_portrait(input_text, output_path, title_header_og="###문서제목", title_header_nw="# 문서제목", font_path="c:/Windows/Fonts/malgun.ttf", font_size=7, font_size_title=12):
    '''
    Export plain text with Markdown-style tables to PDF with dynamic column width and word-wrap in cells.
    Supports tables both with and without separator rows.
    '''
    try:
        # pdf = FPDF()
        pdf = FPDF(format=(315, 297))
        pdf.add_page()
        pdf.add_font("KoreanFont", fname=font_path, uni=True)

        normal_font_size = 7
        title_font_size = 12
        line_height = 8
        page_width = pdf.w - 2 * pdf.l_margin  # Available width for content

        pdf.set_font("KoreanFont", size=normal_font_size)

        lines = input_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Title header
            if line.startswith(title_header_og):
                pdf.set_font("KoreanFont", size=title_font_size)
                title_text = line.replace(title_header_og, title_header_nw).strip()
                pdf.cell(0, 10, title_text, ln=True)
                pdf.set_font("KoreanFont", size=normal_font_size)
                i += 1
                continue

            # Detect markdown table
            if "|" in line:
                has_separator = (i + 1 < len(lines)) and (set(lines[i + 1].strip()) <= set("|:- "))

                table_lines = [line]
                i += 1

                while i < len(lines) and "|" in lines[i]:
                    # Skip separator row if present
                    if has_separator and i == (lines.index(line) + 1):
                        i += 1
                        continue
                    table_lines.append(lines[i].strip())
                    i += 1

                if len(table_lines) < 1:
                    continue

                if has_separator:
                    headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
                    data_rows = table_lines[1:]
                else:
                    headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
                    data_rows = table_lines[1:]

                rows = []
                for row_line in data_rows:
                    row = [cell.strip() for cell in row_line.split("|") if cell.strip()]
                    if row:
                        rows.append(row)

                num_cols = len(headers)
                max_col_widths = [pdf.get_string_width(header) for header in headers]

                for row in rows:
                    for j in range(num_cols):
                        cell = row[j] if j < len(row) else ""
                        cell_width = pdf.get_string_width(cell)
                        if cell_width > max_col_widths[j]:
                            max_col_widths[j] = cell_width

                total_width = sum(max_col_widths)
                scale = page_width / total_width if total_width > 0 else 1
                scaled_col_widths = [w * scale for w in max_col_widths]

                # Render header
                for j, header in enumerate(headers):
                    pdf.cell(scaled_col_widths[j], line_height, txt=header, border=1)
                pdf.ln(line_height)

                # Render rows with word wrap
                for row in rows:
                    # Pad row to num_cols with empty strings if shorter
                    if len(row) < num_cols:
                        row += [''] * (num_cols - len(row))

                    cell_heights = []
                    for j in range(num_cols):
                        cell = row[j]
                        col_w = scaled_col_widths[j]

                        if not cell:
                            # Empty cell minimum height
                            cell_heights.append(line_height)
                            continue

                        str_width = pdf.get_string_width(cell)
                        lines_needed = max(1, math.ceil(str_width / col_w))
                        cell_heights.append(lines_needed * line_height)

                    if not cell_heights:
                        continue

                    max_cell_height = max(cell_heights)

                    # Page break check
                    if pdf.get_y() + max_cell_height > pdf.page_break_trigger:
                        pdf.add_page()
                        # Reprint header on new page
                        for j, header in enumerate(headers):
                            pdf.cell(scaled_col_widths[j], line_height, txt=header, border=1)
                        pdf.ln(line_height)

                    x_start = pdf.get_x()
                    y_start = pdf.get_y()

                    for j in range(num_cols):
                        cell = row[j]
                        w = scaled_col_widths[j]
                        h = max_cell_height

                        x = pdf.get_x()
                        y = pdf.get_y()

                        pdf.rect(x, y, w, h)
                        pdf.set_xy(x, y)
                        pdf.multi_cell(w, line_height, cell)
                        pdf.set_xy(x + w, y)

                    pdf.set_xy(x_start, y_start + max_cell_height)

                pdf.ln(line_height)
                continue

            # Normal text line
            if line:
                pdf.multi_cell(0, line_height, line)
            else:
                pdf.ln(line_height)
            i += 1

        pdf.output(output_path)
    except Exception as e:
        import traceback
        print(f"** Error *******************************\n****************************************\n{e}")
        traceback.print_exc()





def to_pdf_landscape(input_text, output_path, title_header_og="###문서제목", title_header_nw="# 문서제목", font_path="c:/Windows/Fonts/malgun.ttf"):
    '''
    Export plain text with Markdown-style tables to PDF with dynamic column width.
    Supports tables both with and without separator rows.
    PDF page size is A4 Landscape (wider).
    '''
    try:
        # Create PDF with A4 Landscape for wider page
        pdf = FPDF(orientation='L', format='A4')
        pdf.add_page()
        pdf.add_font("KoreanFont", fname=font_path, uni=True)

        normal_font_size = 7
        title_font_size = 12
        line_height = 8
        page_width = pdf.w - 2 * pdf.l_margin  # Available width for content

        pdf.set_font("KoreanFont", size=normal_font_size)

        lines = input_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Title header
            if line.startswith(title_header_og):
                pdf.set_font("KoreanFont", size=title_font_size)
                title_text = line.replace(title_header_og, title_header_nw).strip()
                pdf.cell(0, 10, title_text, ln=True)
                pdf.set_font("KoreanFont", size=normal_font_size)
                i += 1
                continue

            # Detect markdown table
            if "|" in line:
                has_separator = (i + 1 < len(lines)) and (set(lines[i + 1].strip()) <= set("|:- "))

                table_lines = [line]
                i += 1

                while i < len(lines) and "|" in lines[i]:
                    if has_separator and i == (lines.index(line) + 1):
                        i += 1
                        continue
                    table_lines.append(lines[i].strip())
                    i += 1

                if len(table_lines) < 1:
                    continue

                if has_separator:
                    headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
                    data_rows = table_lines[1:]
                else:
                    headers = [cell.strip() for cell in table_lines[0].split("|") if cell.strip()]
                    data_rows = table_lines[1:]

                rows = []
                for row_line in data_rows:
                    row = [cell.strip() for cell in row_line.split("|") if cell.strip()]
                    if row:
                        rows.append(row)

                num_cols = len(headers)

                # Calculate max string width per column (header + rows)
                max_col_widths = [pdf.get_string_width(header) for header in headers]
                for row in rows:
                    for j in range(num_cols):
                        cell = row[j] if j < len(row) else ""
                        cell_width = pdf.get_string_width(cell)
                        if cell_width > max_col_widths[j]:
                            max_col_widths[j] = cell_width

                total_width = sum(max_col_widths)
                scale = page_width / total_width if total_width > 0 else 1
                scaled_col_widths = [w * scale for w in max_col_widths]

                # Render header
                for j, header in enumerate(headers):
                    pdf.cell(scaled_col_widths[j], line_height, txt=header, border=1)
                pdf.ln(line_height)

                # Render rows
                for row in rows:
                    for j in range(num_cols):
                        cell = row[j] if j < len(row) else ""
                        pdf.cell(scaled_col_widths[j], line_height, txt=cell, border=1)
                    pdf.ln(line_height)

                pdf.ln(line_height)
                continue

            # Normal text line
            if line:
                pdf.multi_cell(0, line_height, line)
            else:
                pdf.ln(line_height)
            i += 1

        pdf.output(output_path)

    except Exception as e:
        print(f"** Error *******************************\n****************************************\n{e}")

