# Data Pipeline SDK

Data Pipeline SDK is a Python prototype for reusable data-pipeline building blocks: ingestion, transformation, output, plugin extension, logging, metrics and error handling.

## Current repository state

The repository contains working Python modules and pytest coverage for several SDK concepts, including:

- pipeline orchestration
- Kafka-oriented ingestion foundations
- JSON/XML transformation helpers
- output/serialisation helpers
- plugin interfaces and plugin loading
- standard and Datadog-oriented logging
- Prometheus-style metrics integration
- configuration and error-handling utilities

The project is retained as a **library/tooling asset**, but it is not yet packaged as a modern installable Python SDK. The current source layout is flat and dependency management is still based on `requirements.txt`.

## Development

Create an isolated Python environment, install the current dependencies, then run the tests:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Ruff is included in the development dependencies and can be run with:

```bash
ruff check .
```

## Architecture direction

`SDK_Project_Guide.md` describes the broader intended SDK scope. Future development should preserve small, explicit interfaces between ingestion, transformation, output and plugin concerns rather than turning the SDK into one framework-coupled pipeline implementation.

## Modernisation priorities

Before treating this as a distributable SDK:

1. introduce `pyproject.toml` and a proper import package under `src/`
2. define a stable public API and semantic versioning policy
3. separate optional Kafka/Datadog/metrics dependencies from the core package
4. add CI for linting, tests and supported Python versions
5. add integration tests for Kafka and plugin loading
6. document configuration contracts and failure behaviour
7. build and inspect wheel/sdist artefacts before publishing

The existing flat modules should be migrated deliberately so downstream imports are not broken accidentally.

## Licence

See `LICENSE`.
