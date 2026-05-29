# pyPORIS_user

This repository is a working area for PORIS instrument models. It is meant to be
forked by users who want to keep their own models under version control while
using the `pyPORIS` toolchain as a submodule.

Models live under `models/`. Generated products live under `output/`:

```text
output/py/    generated Python model classes and editable physical companions
output/xml/   XML files loaded by the Java Swing panel
output/ods/   optional spreadsheet products
```

The current generation flow is centered on Python: GraphML is parsed into a
Python PORIS model, and the XML panel file is generated from that Python model.
The direct XML-from-parser path is kept only as an optional comparison tool.

## Requirements

- Python 3
- Java, for the Swing-based `AstroPorisPlayer`
- Python packages from `requirements.txt`

Recommended setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --no-cache-dir -r requirements.txt
```

The dependency constraints are kept in `constraints.txt` because some parser
dependencies have had breaking changes.

On Debian/Ubuntu-like systems, a suitable Java installation is:

```bash
sudo apt install openjdk-17-jdk
```

## First Checkout

After cloning or forking the repository, initialize the submodule:

```bash
git submodule update --init --recursive
```

This populates `pyPORIS/` and the bundled `AstroPorisPlayer` binaries.

## Quick Start

Open a generated panel for a single GraphML model:

```bash
pyPORIS/porispanel.sh nrt/mainaxis
```

The model argument is the path below `models/`, without the `.graphml`
extension. The command above reads:

```text
models/nrt/mainaxis.graphml
```

and produces:

```text
output/py/mainaxis/mainaxis/mainaxisPORIS.py
output/xml/nrt/mainaxis.xml
```

To generate without opening the panel:

```bash
pyPORIS/porispanel.sh --no-panel nrt/mainaxis
```

To also write the ODS spreadsheet product:

```bash
pyPORIS/porispanel.sh --ods nrt/mainaxis
```

ODS generation is opt-in so normal validation runs do not rewrite spreadsheet
products unnecessarily.

## User Guide

For the normal modeling workflows, see:

```text
docs/user-guide.md
```

That guide covers:

- single-file models
- directory/supramodel models
- XML generation from Python
- optional parser XML comparison
- visual validation of all panels
- generated Python and editable physical code

## Main Commands

Single GraphML model:

```bash
pyPORIS/porispanel.sh [--ods] [--parser-xml] [--no-panel] <model>
```

Fragmented directory model:

```bash
pyPORIS/porispanel_dir.sh [--ods] [--parser-xml] [--no-panel] <model-dir>
```

cosmoSys variants:

```bash
pyPORIS/porispanel_csys.sh <model>
pyPORIS/porispanel_dir_csys.sh <model-dir>
```

Open an existing XML directly:

```bash
pyPORIS/xmlporispanel.sh output/xml/nrt/mainaxis.xml
```

Generate or run the Python physical model:

```bash
pyPORIS/doPorisPython.sh nrt/mainaxis
pyPORIS/runPorisModel.sh nrt/mainaxis
```

Run a visual validation pass over all known panels:

```bash
pyPORIS/test_porispanels.sh
```

Close each `AstroPorisPlayer` window to continue with the next model.

## Updating pyPORIS

`pyPORIS/` is a git submodule pinned by this repository. To update it manually:

```bash
cd pyPORIS
git fetch --all
git checkout main
git pull
cd ..
git add pyPORIS
git commit -m "Update pyPORIS submodule"
```

Toolchain behavior can change over time, so validate the generated products
after moving the submodule.

## Notes

The `models/` directory should contain source models only. Generated Python,
XML and ODS products should be kept under `output/`.


Happy modeling!

cosmoBots.eu
