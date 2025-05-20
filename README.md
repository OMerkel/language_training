# Language Training

Some tools to support you on your language training stuff.

## Setup

Clone the repository locally and have Python installed.

* Create a Python virtual environment.

```bash
python -m venv .venv
```

* Activate the Python virtual environment
* Update pip
* Install packages from requirements.txt
* Check uv version
* Sync and resolve package dependencies

```bash
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
uv --version
uv sync
```

Now you can run any given script from this repository, e.g. ...

```bash
uv run read_out_loud.py
```
