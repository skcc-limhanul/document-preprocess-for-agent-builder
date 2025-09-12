# Document Parser for Agent Builder

### 목적
* A.Biz의 Agent Builder에서 사용자 질의에 좋은 답변(결과물)을 얻기 위함
* 원 문서의 정보(문자, 표 등)를 최대한 보존하기 위함
  * 사용자 질의와 유사도가 높은 문서를 Retrieve 할때, 원 문서와 유사한 정보가 있어야 좋은 답변을 얻을 수 있음

### 기능
* DOCX, PPTX, XLSX, PDF 형식의 문서를 Plain Text로 변환
* 문서의 순서를 유지하면서, 글자 및 표 변환
  * 글자는 원 문서에 있는 내용과 순서를 그대로 보존하면서 글자 추출
  * 표는 형태를 최대한 유지하면서 Markdown과 유사한 방법으로 추출
* 복수개의 문서가 존재하는 경우, 문서를 묶어서 Parsing 처리
  * e.g. 120개 문서를 30개씩 묶어서 1개씩 TXT Format 4개로 변환 가능
* 미지원 형식 (Legacy MS Office 형식으로 인하여, Parsing 불가능)
  * DOC, PPT, XLS
