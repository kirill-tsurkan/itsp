Set up for development
=======

1. Install Python and pip
    Make sure Python is added to PATH environment

2. Install virtualenv using pip:
    `pip install virtualenv`

3. Create virtual environment in project root:
    `virtualenv venv`

4. Activate virtual environment:
    Windows:
    `.\venv\Scripts\activate`

    Linux:
    `source ./venv/bin/activate`

    type `deactivate` to deactivate virtualenv

5. Make sure your venv is active:
    `pip -V` it should show current python interpreter in use. Must be the one inside project's `venv` folder.

6. Install requirements:
    `pip install -r requirements.txt`

Make sure you **always** use virtual environment before doing something in terminal.
You can check for current environment with: `pip -V`. It should show current python interpreter in use. Must be the one inside project's `venv` folder.

https://docs.getpelican.com/en/stable/index.html

Commands
------
pelican --help      # help
pelican content     # generate output files
pelican -r          # watch for changes in files
pelican --listen    # run devserver at 127.0.0.1:8000
