# Language Training

[![Pylint](https://github.com/OMerkel/language_training/actions/workflows/pylint.yml/badge.svg)](https://github.com/OMerkel/language_training/actions/workflows/pylint.yml)
[![uv](https://img.shields.io/badge/uv-fast%20Python%20package%20manager-blue)](https://docs.astral.sh/uv/)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://docs.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/OMerkel/language_training/blob/main/LICENSE)

Some tools to support you on your language training stuff.

## Tool Overview

- **read_out_loud.py** This script reads out loud a language training text from a data/*.toml in target language using the gTTS (Google Text-to-Speech) library.

## Setup

Clone the repository locally and have Python installed.

- Create a Python virtual environment.

```bash
python -m venv .venv
```

- Activate the Python virtual environment
- Update pip
- Install packages from requirements.txt
- Check uv version
- Sync and resolve package dependencies

```bash
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
uv --version
uv sync
```

## Run some Tools

Now you can run any given script from this repository, e.g. ...

- run read_out_loud.py and show the usage information

```bash
uv run read_out_loud.py --help
```

- run read_out_loud.py using default parameters

```bash
uv run read_out_loud.py
```

- run read_out_loud.py showing text in Italian waiting for a keypress then
  showing the Japanese version and read it out loud.

```bash
uv run .\read_out_loud.py --source_lang it-IT --target_lang ja-JP --toml_file .\data\greetings.toml
```

## Current Language Support

Use the mentioned Country Codes to refer to your intended language selection.

| Flag | Country Name      | Country Code |
|------|-------------------|--------------|
| ![German Flag](./img/flag_de-DE.svg)     | Germany       | de-DE           |
| ![US Flag](./img/flag_en-US.svg)         | United States | en-US           |
| ![French Flag](./img/flag_fr-FR.svg)     | France        | fr-FR           |
| ![Spanish Flag](./img/flag_es-ES.svg)    | Spain         | es-ES           |
| ![Italian Flag](./img/flag_it-IT.svg)    | Italy         | it-IT           |
| ![Portuguese Flag](./img/flag_pt-PT.svg) | Portugal      | pt-PT           |
| ![Russian Flag](./img/flag_ru-RU.svg)    | Russia        | ru-RU           |
| ![Japanese Flag](./img/flag_ja-JP.svg)   | Japan         | ja-JP           |
| ![Chinese Flag](./img/flag_zh-CN.svg)    | China         | zh-CN           |
| ![Korean Flag](./img/flag_ko-KR.svg)     | South Korea   | ko-KR           |
| ![Dutch Flag](./img/flag_nl-NL.svg)      | Netherlands   | nl-NL           |
| ![Swedish Flag](./img/flag_sv-SE.svg)    | Sweden        | sv-SE           |
| ![Turkish Flag](./img/flag_tr-TR.svg)    | Turkey        | tr-TR           |
| ![Polish Flag](./img/flag_pl-PL.svg)     | Poland        | pl-PL           |
