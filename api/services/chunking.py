import re
import pdfplumber
from typing import List, Dict, Any


def chunk_document_by_section(file_path: str) -> List[Dict[str, Any]]:
    chunks = []
    current_section = None
    current_subsection = None

    with pdfplumber.open(file_path) as pdf:
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
                        # 소제목 없이 본문이 이어질 경우
                        if not current_section.get("content"):
                            current_section["content"] = ""
                        current_section["content"] += line + "\n"

            # 페이지의 테이블을 현재 소제목 또는 섹션에 추가
            for table in tables:
                table_str = "\n".join([" | ".join([str(cell) if cell is not None else "" for cell in row]) for row in table])
                if current_subsection:
                    current_subsection["tables"].append(table_str)
                elif current_section:
                    if "tables" not in current_section:
                        current_section["tables"] = []
                    current_section["tables"].append(table_str)

    # 마지막 섹션 저장
    if current_section:
        chunks.append(current_section)

    return chunks
