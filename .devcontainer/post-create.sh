# Install dependencies
poetry install --with dev,docs

# Activate environment
sh ./.venv/bin/activate

# Install pre-commit hooks
pre-commit install

# Login into GCP
gcloud auth application-default login
