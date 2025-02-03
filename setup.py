from setuptools import setup, find_packages

setup(
    name="yoobee_car_rental",
    version="0.1.0",
    description = "Car rental service package",
    authors = "Thushara Manchanayake",
    author_email = "",
    readme = "README.md",
    license = "MIT",
    packages = find_packages(where="src"),
    package_dir = {"": "src"},
    install_requires = [
        "requests",
        "pytest",
        "alembic",
        "pymysql",
        "pydantic",
        "pydantic[email]",
        "tabulate"
    ],
)
