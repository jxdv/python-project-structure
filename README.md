A skeleton for a python project I use whenever working on a new project. Feel free to use for your own projects.

## Structure

<b>.github directory:</b>

1. `dependabot.yml` - Make sure GitHub actions and Python packages are up-to-date.

workflows:

1. `codeql.yml` - Searching the code for vulnerabilities and bugs.
2. `guarddog.yml` - Scan used Python packages to secure the security of the Supply chain.
3. `lint.yml` - Prevent code smells and make the Python code easy to read.

<b>app_name directory:</b>

1. cli / common / core / db Python local packages - Pretty self-explanatory. More packages can be added based on the purpose of the project.
2. `__init__.py` - Treat it as a package.
3. `__main__.py` - Main CLI entrypoint.
4. `config.py` - Loads secrets / app configuration from environment files etc.
5. `exceptions.py` - Defining custom exceptions for the project.

<b>Environment files</b>

1. `.env` - Shared environment file.
2. `.env.dev` - Environment file for dev purposes.

<b>Requirements files</b>

1. `requirements.txt` - Requirements for the actual project.
2. `requirements-dev.txt` - Requirements for test / dev purposes.

<b>GitHub miscellaneous</b>

1. `.gitignore` - Exclude files from working repository.
2. `README.md` - Describe what the project actually does.
3. `LICENSE` - License for the project.

<b>Other</b>

1. `ruff.toml` - Configuration for [Ruff](https://github.com/astral-sh/ruff).
2. `Dockerfile` - Project build instructions for Docker.
