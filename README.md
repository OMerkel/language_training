# Language Training

![https://github.com/OMerkel/language_training/actions/workflows/pylint.yml](https://github.com/OMerkel/language_training/actions/workflows/pylint.yml/badge.svg)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

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
