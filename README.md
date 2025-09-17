# Document Parser for DOCX / PPTX / XLSX / PDF

### Purpose
* This is a document parser to extract texts and tables from documents files such as MS Word, Power Point, Excel and PDF
* In the case of extracting tables from documents
  * It reconstructs tables for preserving the structure of tables from DOCX / PPTX / XLSX / PDF
  * It is good to retreive documents that are similar to user's query with reconstructed tables

### Function
* Document Parser can
  * Converts DOCX / PPTX / XLSX / PDF to plain text
    * Not support Legacy MS Office document such as DOC / PPT / XLS
    * Not support encrypted documents
    * Not support OCR from images
  * Preserve the orders of texts, tables during document parsing
  * Reconstruct tables from documents to markdown style tables
  * Bind multiple documents into a few or one plain text documents
    * e.g. Create 10 plain text documents from 160 original documents

### How to Use function
* Function : parse_content
  * Parameter
    * file_path (String) : The path of original documents (e.g. c:/temporary/original/documents.pptx)
  * Return
    * parsed_text (String) : Plain text with texts and markdown style tables from original documents
  * Example of usage
    ```
    from parser import docx, pdf, pptx, xlsx
    print(docx.parse_content("c:/temporary/original/documents.pptx"))
    ```
  * Result of usage
    ```
    | 항목 | 비고 |
    | --- | --- |
    | 식사 및 다과 | 휴게시간으로 등록 |
    | 개인시간 | 휴게시간으로 등록 (흡연, 병원 등) |
    | 재택근무 | 원칙적으로 인정하지 않음
    특별한 경우 리더 승인 하 인정
    (현재 임원조직별 일시적 자율 운영중) |
    | 사전 협의되지 않은 야근 / 주말근무 | 근로 시간 인정 X |
    | 개인 업무 준비시간 |  |
    | 사내/외 회식 |  |
    | 직무 外 교육 |  |
    | 사내 경조사 |  |
    ※ 임산부 검진은 휴가로 등록
    ※ 건강검진 근무형태(사내근무/사외근무/교육/출장/건강검진) 로 입력

    3. Q&A 및 사용 Guide
    1일 최대 근무 한도는 12시간 이내로 권장합니다. 
    효과적인 업무 몰입과 건강 관리를 위해 12시간을 초과하는 업무는 지양하여 주시기 바랍니다.
    ```

### How to Use Script for multiple Documents
* Script : parse_documents.py
  * Variables
    * input_path : The path of document files (e.g. c:/temporary/original/)
    * output_path : the path of output documents directory (e.g. c:/temporary/parsed/)
    * file_name_to_export : File names of output texts
      * e.g. documents_parsed
        * Result : documents_parsed_01.txt, documents_parsed_02.txt, documents_parsed_03.txt ...
    * max_output : The number of output documents (deafult : 10)
      * e.g. max_output = 2
        * Result : documents_parsed_01.txt, documents_parsed_02.txt (There are 2 plain texts outputs)
      * If the number of original documents is less than max_output, the number of output documents will be the number of original documents
