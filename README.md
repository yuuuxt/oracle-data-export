# readme

## setup

- install `uv`
    - direct way (suppose using Windows)
        - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
    - indirect way
        - install python from [official website](https://www.python.org/downloads/)
        - install `pipx`:
            - `python -m pip install --user pipx`
            - `python -m pipx ensurepath`
        - install `uv`:`pipx install uv`
- project setup:
    - install deps: `uv sync`
    - setup `Oracle Instant Client` - Oracle 11.2 requires `thick mode`
        - download  from [official website](https://www.oracle.com/apac/database/technologies/instant-client/winx64-64-downloads.html)
            - `Basic Light Package` is OK
        - create `.env` file and setup `INSTANTCLIENT_PATH`
    - adjust the connection accordingly
        - check [doc](https://python-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html)

## usage

- create scripts in scripts folder, and run: `uv run scripts\<script-name>.py`
    - check the scripts folder for an export example.
