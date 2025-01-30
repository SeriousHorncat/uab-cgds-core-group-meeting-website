# CGDS Website HTML Publication Generator 📚🖥️✨

<!-- markdown-link-check-disable -->
[![Perform linting -
Markdown](https://github.com/SeriousHorncat/uab-cgds-core-group-meeting-website/actions/workflows/linting.yml/badge.svg)](https://github.com/SeriousHorncat/uab-cgds-core-group-meeting-website/actions/workflows/linting.yml) [![Python CI](https://github.com/SeriousHorncat/uab-cgds-core-group-meeting-website/actions/workflows/python.yml/badge.svg)](https://github.com/SeriousHorncat/uab-cgds-core-group-meeting-website/actions/workflows/python.yml) <!-- markdownlint-disable-line MD013 -->
<!-- markdown-link-check-enable -->

Python script to generate stylized HTML to insert into CGDS' WordPress website from a ReadCube CSV export of the
Center's publications.

## Requirements

- [Python 3.11+](https://www.python.org/) - [Install](https://www.python.org/downloads/)

## How to run

1. Move your TSV exported from ReadCube `publications.csv` to the `config` directory and name it `publications.csv`.
2. Run in terminal

   ```bash
   python3 src/generate_html.py
   ```
