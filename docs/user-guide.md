# pyPORIS User Guide

This guide describes the normal workflows in this repository. It assumes
commands are executed from the repository root.

## Repository Layout

Source models are kept in `models/`.

Generated products are kept in `output/`:

```text
output/py/<model>/<model>/<model>PORIS.py
output/py/<model>/<model>_physical/<model>_physical.py
output/xml/<path>/<model>.xml
output/ods/<path>/<model>.ods
```

The generated `*PORIS.py` file is automatic code. The `*_physical.py` file is
the editable companion where user behavior can live.

## Single GraphML Models

A single model is a `.graphml` file under `models/`.

For example:

```text
models/nrt/mainaxis.graphml
```

is addressed as:

```text
nrt/mainaxis
```

Generate Python and XML, then open the panel:

```bash
pyPORIS/porispanel.sh nrt/mainaxis
```

Generate without opening the panel:

```bash
pyPORIS/porispanel.sh --no-panel nrt/mainaxis
```

Also generate the ODS product:

```bash
pyPORIS/porispanel.sh --ods nrt/mainaxis
```

By default, `porispanel.sh` does not generate ODS. This keeps normal validation
runs from rewriting spreadsheet files.

## XML Generation

The primary XML is generated from the generated Python PORIS model:

```text
GraphML -> generated Python -> XML -> AstroPorisPlayer
```

The parser XML path is still available for comparison:

```bash
pyPORIS/porispanel.sh --ods --parser-xml --no-panel nrt/mainaxis
```

This produces:

```text
output/xml/nrt/mainaxis.xml
output/xml/nrt/mainaxis.from-parser.xml
output/xml/nrt/mainaxis.xml.diff
```

`--parser-xml` requires `--ods`, because the parser XML is generated from the
ODS product.

## Opening Existing XML

To inspect an XML that already exists:

```bash
pyPORIS/xmlporispanel.sh output/xml/nrt/mainaxis.xml
```

## Visual Validation

To launch all known panels one by one:

```bash
pyPORIS/test_porispanels.sh
```

The script opens a panel and waits until the Java process exits. Close the
current `AstroPorisPlayer` window to continue with the next model.

Useful variants:

```bash
pyPORIS/test_porispanels.sh --with-csys
pyPORIS/test_porispanels.sh --ods
pyPORIS/test_porispanels.sh --no-prompt
pyPORIS/test_porispanels.sh --no-panel --no-prompt
```

The last form is useful as a generation smoke test.

## Python Models And Physical Code

Generate Python products:

```bash
pyPORIS/doPorisPython.sh nrt/mainaxis
```

Run the physical companion:

```bash
pyPORIS/runPorisModel.sh nrt/mainaxis
```

`doPorisPython.sh` regenerates the automatic Python model but preserves an
existing physical directory. If the physical companion does not exist, it is
created from the template.

Commands modeled as `prCmd` nodes are exposed as callable methods in Python.
If no custom behavior is registered, the generated behavior logs a default
execution trace. The physical companion is the intended place to override or
register real behavior.

## Directory Models And Supramodels

A directory model is a model split across several `.graphml` files in the same
folder. The current example is:

```text
models/osiris/
```

Open it as a combined model:

```bash
pyPORIS/porispanel_dir.sh osiris
```

Generate it without opening the panel:

```bash
pyPORIS/porispanel_dir.sh --no-panel osiris
```

The important idea is that each file is both an independent project fragment and
part of a larger root model. The generator reads all `.graphml` files in the
directory, normalizes node paths, resolves external references, and emits a
single Python/XML model.

For a directory to behave as a supramodel:

- The directory name is the root model name passed to `porispanel_dir.sh`.
- One GraphML file should normally share that root name, for example
  `models/osiris/osiris.graphml`.
- Each GraphML graph declares an `identifier` value. In `osiris`, files declare
  identifiers such as `osiris`, `osiopt`, `osidas`, `osifp`, `osifilt` and
  `osigeom`.
- Each GraphML graph declares a `rootid`. For the fragments in `osiris`, this is
  `osiris`.
- Each non-root GraphML graph declares a `parentid`, naming the project that
  contains or references it.
- Nodes carry a `project` value. When a node appears in a file but its `project`
  points to another identifier, the generator treats it as an external reference
  or alias, not as a duplicate owned node.
- The same logical node can appear as an alias in a parent fragment and as the
  real owned node in its own fragment. The generator merges those appearances by
  global path.

In practice, this lets a top-level diagram contain a high-level placeholder for
a subsystem while the subsystem is described in detail in another `.graphml`
file.

Not every directory under `models/` is a supramodel. For example,
`models/example/` contains several independent examples, so it should be tested
with `porispanel.sh example/<name>`, not with `porispanel_dir.sh example`.

## cosmoSys Variants

The `*_csys.sh` commands enable cosmoSys synchronization:

```bash
pyPORIS/porispanel_csys.sh nrt/mainaxis
pyPORIS/porispanel_dir_csys.sh osiris
```

Before using them, configure the cosmoSys credentials from the provided example
configuration files under `pyPORIS/`.

## Generated Product Policy

Keep source models in `models/`.

Generated products should go to:

```text
output/py/
output/xml/
output/ods/
```

The current preferred XML product is `<model>.xml`, generated from Python. Older
`*.from-python.xml` products are historical artifacts from the transition period.

## Troubleshooting

If a panel opens with the wrong root system, check that the generated Python
model instantiates the intended root and that the XML was generated from that
model.

If a directory model fails, first verify it is really a supramodel and not just a
folder of independent examples. The fragments should have coherent `identifier`,
`rootid`, `parentid` and node `project` values.

If parser XML comparison fails because an ODS file is missing, rerun with
`--ods --parser-xml`.
