# Tengen

Tengen is based on the "Labosphere" in the repository this one is forked from. It generates [Cubari](https://cubari.moe) repositories for *Jujutsu Kaisen* releases by [TCB Scans](https://tcbscans.com).

It retrieves chapter metadata in reverse sequential order, beginning with the latest chapter and ending with Chapter 1.
It then uses this metadata to compose a JSON file which can be provided to Cubari as-is.

The technically inclined are welcome to run Tengen themselves:

```bash
docker run -v ${PWD}/tengen:/tengen -t ghcr.io/mcradcliffe/tengen:latest
```

Or, if you prefer the hard way (Python 3.11 or later and [Poetry](https://python-poetry.org) required):

```bash
git clone https://github.com/mcradcliffe/hidden-inventory
cd hidden-inventory/tengen
poetry install --only main
poetry run tengen start
```