import re
import pdfplumber
from typing import List, Dict, Any
from fastapi import UploadFile
import os
import tempfile


def extract_chunks_from_pdf_upload(uploaded_file: UploadFile) -> List[Dict[str, Any]]:
    chunks = []
    current_section = None
    current_subsection = None

    # 파일 임시 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.file.read())
        tmp_path = tmp.name

    with pdfplumber.open(tmp_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            tables = page.extract_tables()

            lines = text.split("\n")
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                # 대제목 (예: "1. 사업 개요")
                if re.match(r"^\d+\.\s", line):
                    if current_section:
                        chunks.append(current_section)
                    current_section = {
                        "section_title": line,
                        "subsections": []
                    }
                    current_subsection = None

                # 소제목 (예: "□ 신청대상")
                elif re.match(r"^[\u25A0\u25CB\u25CF\u25AA\u25AB\u25B2\-\u2022\u2219\u25E6□\-○]+", line):
                    current_subsection = {
                        "subtitle": line,
                        "content": "",
                        "tables": []
                    }
                    if current_section:
                        current_section["subsections"].append(current_subsection)

                # 본문 텍스트
                else:
                    if current_subsection:
                        current_subsection["content"] += line + "\n"
                    elif current_section:
                        if not current_section.get("content"):
                            current_section["content"] = ""
                        current_section["content"] += line + "\n"

            for table in tables:
                table_str = "\n".join([
                    " | ".join([str(cell) if cell is not None else "" for cell in row])
                    for row in table
                ])
                if current_subsection:
                    current_subsection["tables"].append(table_str)
                elif current_section:
                    if "tables" not in current_section:
                        current_section["tables"] = []
                    current_section["tables"].append(table_str)

    if current_section:
        chunks.append(current_section)

    os.remove(tmp_path)  # 임시 파일 삭제
    return chunks
