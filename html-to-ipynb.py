import json
from bs4 import BeautifulSoup

# Load the HTML file
with open("08-interpolation-basics.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Extract code blocks
codes = []
for block in soup.find_all(["pre", "code", "div"], class_=["highlight", None]):
    text = block.get_text().strip()
    if text and len(text.split()) > 1:  # ignore empty or single-word junk
        codes.append(text)

# Build ipynb structure
notebook = {
    "cells": [
        {
            "cell_type": "code",
            "metadata": {},
            "source": code.splitlines(True),  # preserve line breaks
            "outputs": [],
            "execution_count": None
        }
        for code in codes
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "file_extension": ".py"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

# Save notebook
with open("08-interpolation-basics.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print(f"✅ Converted {len(codes)} code blocks into notebook cells")