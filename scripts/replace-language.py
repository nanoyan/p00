import yaml
import re
from pathlib import Path

# Paths
input_qmd = Path("index.qmd")
language_file = Path("scripts/replace-to-tags.yml")
output_qmd = Path("scripts/template.txt")

# Read files
qmd_text = input_qmd.read_text(encoding="utf-8")
language_dict = yaml.safe_load(language_file.read_text(encoding="utf-8"))

# Replace words (whole-word matching)
for source, target in language_dict.items():
    pattern = rf"\b{re.escape(source)}\b"
    qmd_text = re.sub(pattern, target, qmd_text)

# Write new file
output_qmd.write_text(qmd_text, encoding="utf-8")

print(f"Created translated file: {output_qmd}")