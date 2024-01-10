from setuptools import setup, find_packages

setup(
    name="sf_data_integration",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "requests",
        "sqlalchemy",
        "psycopg2-binary",
        "simple-salesforce",
    ],
    entry_points={
        "console_scripts": [
            "sf-data-cli=cli_backend.core.main:main"
        ],
    },
)
