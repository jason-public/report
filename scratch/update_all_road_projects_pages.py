import json
import re

# Update build_final_dataset.py to map proj-6 through proj-13 to their exact 2-page pairs

mapping = {
    "proj-1": {"pdfPage": 6, "pdfPages": [6], "pdfPageLabel": "P.6"},
    "proj-2": {"pdfPage": 7, "pdfPages": [7], "pdfPageLabel": "P.7"},
    "proj-3": {"pdfPage": 8, "pdfPages": [8], "pdfPageLabel": "P.8"},
    "proj-4": {"pdfPage": 9, "pdfPages": [9, 10], "pdfPageLabel": "P.9~10"},
    "proj-5": {"pdfPage": 11, "pdfPages": [11, 12, 13], "pdfPageLabel": "P.11~13"},
    "proj-6": {"pdfPage": 14, "pdfPages": [14, 15], "pdfPageLabel": "P.14~15"},
    "proj-7": {"pdfPage": 16, "pdfPages": [16, 17], "pdfPageLabel": "P.16~17"},
    "proj-8": {"pdfPage": 18, "pdfPages": [18, 19], "pdfPageLabel": "P.18~19"},
    "proj-9": {"pdfPage": 20, "pdfPages": [20, 21], "pdfPageLabel": "P.20~21"},
    "proj-10": {"pdfPage": 22, "pdfPages": [22, 23], "pdfPageLabel": "P.22~23"},
    "proj-11": {"pdfPage": 24, "pdfPages": [24, 25], "pdfPageLabel": "P.24~25"},
    "proj-12": {"pdfPage": 26, "pdfPages": [26, 27], "pdfPageLabel": "P.26~27"},
    "proj-13": {"pdfPage": 28, "pdfPages": [28, 29], "pdfPageLabel": "P.28~29"}
}

print("Mappings configured:")
for k, v in mapping.items():
    print(f"  {k}: {v}")
