import fitz  # PyMuPDF
import sys
import glob

def count_references(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    
    # Find the References section
    # Usually it's "References\n"
    ref_idx = text.rfind("\nReferences\n")
    if ref_idx == -1:
        ref_idx = text.rfind("References\n")
        
    if ref_idx == -1:
        return "References section not found"
        
    ref_text = text[ref_idx:]
    
    # In ACL papers, references often start with the author names.
    # Alternatively, we can just split by double newlines or similar, but
    # pdf text extraction might be messy. Let's just return the length or do a rough count.
    # Actually, a better way is to count the years (e.g., 2020, 2021, 2024) since each reference has a year.
    import re
    years = re.findall(r'\b20\d\d\b|\b19\d\d\b', ref_text)
    
    # This might overcount if titles have years, but gives an estimate.
    # A more robust way: count occurrences of "ArXiv" or "arXiv" or "Proceedings" or "Journal" combined with a year.
    # Or just return the raw text to let me inspect it.
    
    return len(years)

pdfs = glob.glob("/Users/tazwar/.gemini/antigravity-ide/brain/99159b0e-a126-4e35-baa0-9b271dfb6412/.user_uploaded/*.pdf")
for p in pdfs:
    print(f"{p}: {count_references(p)} references (approx)")

