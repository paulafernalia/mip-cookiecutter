install:
	uv pip install -e .

run:
	uv run -m {{cookiecutter.package_name}}

ruff:
	uv run ruff check --fix

test:
	uv run pytest --cov=src

hooks:
	uv run pre-commit install
	uv run pre-commit run --all-files

check-template:
	uv run cruft check

update-template:
	uv run cruft update