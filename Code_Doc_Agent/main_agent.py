import uuid
import os
from repo_scan import scan_repository
from code_parser import parse_python_file
from Documentation_agent import analyze_code
from generate_docx import generate_docx
from Vector_store import store_chunk

REPO_PATH = str(input("Enter the path to the code repository: "))

def main():

    files = scan_repository(REPO_PATH)

    all_results = []

    for file_path in files:

        print(f"Analyzing {file_path}")

        try:

            parsed = parse_python_file(file_path)
            code = parsed["code"]

            store_chunk(str(uuid.uuid4()),code)

            analysis = analyze_code(code)

            all_results.append({"file": file_path,"analysis": analysis})

        except Exception as e:

            print(e)

    generate_docx(all_results,"project_report.docx")

    print("DONE")

if __name__ == "__main__":
    main()