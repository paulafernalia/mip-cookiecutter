run:
	uv run -m {{cookiecutter.package_name}}

install:
	uv pip install -e .

ruff:
	uv run ruff check

test:
	uv run pytest --cov=src

mypy:
	uv run mypy src/

complexipy:
	uv run complexipy src/

hooks:
	uv run pre-commit install
	uv run pre-commit run --all-files

bandit:
	uv tool run bandit -ll src
