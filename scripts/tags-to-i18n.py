import yaml
import re
from pathlib import Path

# Paths
i18n_dir = Path("i18n")
input_qmd = Path("scripts/template.txt")
output_dir = Path("output")

translations = {}

for yml_file in i18n_dir.glob("*.yml"):
    lang = yml_file.stem
    output_qmd = output_dir / f"{lang}.qmd"
    with yml_file.open("r", encoding="utf-8") as f:

        translations[lang] = yaml.safe_load(f)
        qmd_text = input_qmd.read_text(encoding="utf-8")
        # Replace words (whole-word matching)
        for source, target in translations[lang].items():
            pattern = rf"\b{re.escape(source)}\b"
            qmd_text = re.sub(pattern, target, qmd_text)

    # Write new file
    output_qmd.write_text(qmd_text, encoding="utf-8")
    print(f"Created translated file: {output_qmd}")
   