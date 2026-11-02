# pyPORIS User Guide

This guide describes the normal workflows in this repository. It assumes
commands are executed from the repository root.

## Repository Layout

Source models are kept in `models/`.

Generated products are kept in `output/`:

```text
output/py/<source-directory>/<model>PORIS.py
output/py/<source-directory>/<model>_physical/<model>_physical.py
output/xml/<path>/<model>.xml
output/ods/<path>/<model>.ods
```

The generated `*PORIS.py` file is automatic code. The `*_physical.py` file is
the editable companion where user behavior can live.

## Bash Model Completion

Enable model completion in the current Bash terminal, from the repository root:

```bash
source pyPORIS/scripts/poris-completion.bash
```

Typing `pyPORIS/porispanel.sh osi` and pressing Tab completes `osiris/`.
Continue typing and pressing Tab to explore its GraphML models; file names
are completed without `.graphml`. Press Tab twice to list ambiguous choices.
Directories keep their trailing slash so you can continue browsing, or press
Enter to generate the directory model using its `cluster.yaml`.

Completion also works for `porispanel_csys.sh`, `porispanel_dir.sh` and
`porispanel_dir_csys.sh`, including options such as `--no-panel`. Directory
variants suggest only directories. Candidates come from `models/` under the
current working directory, not from generated outputs or cluster names.

To enable it in future Bash terminals, add a `source` command using the absolute
path to `pyPORIS/scripts/poris-completion.bash` to your `~/.bashrc`.
No additional completion package is required.

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

Generate Python and XML, then open the Vue web viewer:

```bash
pyPORIS/porispanel.sh --web nrt/mainaxis
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

Use `--web` to replace the final Swing panel with the Vue viewer:

```text
GraphML -> generated Python -> XML -> porisViewer
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
pyPORIS/xmlporispanel.sh --web output/xml/nrt/mainaxis.xml
```

## Vue Web Viewer

The `--web` option opens the generated XML with the Vue viewer in
`pyPORIS/porisViewer` instead of launching the Java Swing panel:

```bash
pyPORIS/porispanel.sh --web nrt/mainaxis
pyPORIS/porispanel_dir.sh --web osiris
pyPORIS/odsporispanel.sh --web nrt/mainaxis
pyPORIS/xmlporispanel.sh --web output/xml/nrt/mainaxis.xml
```

Requirements:

- Node.js and npm must be installed.
- The viewer dependencies must be installed once:

```bash
cd pyPORIS/porisViewer
npm ci
```

When `--web` runs, it copies the generated XML to
`pyPORIS/porisViewer/public/runtime/`, starts the Vite development server on
`127.0.0.1:5173` if needed, and tries to open the default browser. The runtime
copy is ignored by git.

## Visual Validation

To launch all known panels one by one:

```bash
pyPORIS/test_porispanels.sh
```

The script opens a panel and waits until the Java process exits. Close the
current `AstroPorisPlayer` window to continue with the next model.

Useful variants:

```bash
pyPORIS/test_porispanels.sh --with-csys <instance>
pyPORIS/test_porispanels.sh --ods
pyPORIS/test_porispanels.sh --web
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

Directory models may define a cluster descriptor:

```text
models/osiris/cluster.yaml
```

with:

```yaml
cluster: osi
root: osiris
```

`cluster` is the generated composed product name, so the Python class becomes
`osiPORIS` and is written to `output/py/osiris/osiPORIS.py`. `root` is the
GraphML file stem that acts as the root of the composed model, for example
`models/osiris/osiris.graphml`.

If `cluster.yaml` is missing, the command stops and tells you how to create the
descriptor automatically:

```bash
pyPORIS/porispanel_dir.sh --cluster osi osiris
```

If `cluster.yaml` already exists, `--cluster` aborts; edit the descriptor or run
without `--cluster`.

The important idea is that each file is both an independent project fragment and
part of a larger root model. The generator reads all `.graphml` files in the
directory, normalizes node paths, resolves external references, and emits a
single Python/XML model.

For a directory to behave as a supramodel:

- The directory name is the root model name passed to `porispanel_dir.sh`.
- In legacy mode, one GraphML file should normally share that root name, for
  example `models/osiris/osiris.graphml`.
- With `cluster.yaml`, the directory name, generated cluster name and root
  GraphML file can differ. For example, `cluster: osi` and `root: osiris`
  generate `osiPORIS` from the root file `models/osiris/osiris.graphml`.
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
pyPORIS/porispanel_csys.sh <instance> nrt/mainaxis
pyPORIS/porispanel_dir_csys.sh <instance> osiris
```

Configure named instances in `pyPORIS/csys.yaml`, as described below. The old
`config_csys.py` and `config_csys_enabled.py` connection files are no longer read
by the Python tools; no automatic credential migration is performed.

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

## Named cosmoSys Instances and Remote Panels

Install the requirements (including PyYAML), then copy `pyPORIS/csys.yaml.example`
to `pyPORIS/csys.yaml` and edit it. Paths here are relative to the user repository.
The real configuration is ignored by Git; do not put credentials in the example.

```yaml
cosmobots.eu:
  url: https://cosmobots.eu
  ignorecert: false
  key: "YOUR_API_KEY"
localhost:3001:
  url: http://localhost:3001
  ignorecert: false
  key: "YOUR_LOCAL_API_KEY"
```

URLs must include `http://` or `https://`. An empty key allows anonymous access.
Use `PORIS_CSYS_CONFIG=/absolute/path/csys.yaml` to select another configuration;
the remote viewer also accepts `--config PATH`.

Download and open a remote project or item:

```bash
pyPORIS/poriscsyspanel.sh localhost:3001 osiris
pyPORIS/poriscsyspanel.sh localhost:3001 osiris OSIRIS-0006
pyPORIS/poriscsyspanel.sh localhost:3001 osiris 22202
pyPORIS/poriscsyspanel.sh http://localhost:3001/projects/osiris/poris
pyPORIS/poriscsyspanel.sh http://localhost:3001/issues/22202
pyPORIS/poriscsyspanel.sh --web --scope node localhost:3001 osiris 22202
```

The command name is `poriscsyspanel.sh` in both argument forms. URL input selects
credentials by matching the configured server URL (including an installation
subpath); unknown or ambiguous instances are rejected. Query-string `scope` and
`issue_id` are supported on project/PORIS URLs. `--scope` overrides the URL scope.
Credentials in pasted URLs are not used. Redirects are not followed.

Scopes match the server viewer:

- `project`: project and its visible subprojects; default for project input.
- `node_down`: item and descendants; default for item input, including item URLs.
- `node`: the server's focused node view.

CSIDs and numeric issue IDs are resolved through the native item API. For an
item URL, the standard Redmine issue API supplies its project. Both require the
corresponding read permissions. The XML endpoint must support API authentication.
An item in a child project is opened using that item's own project.

The default viewer is Java Swing; `--web` opens the local web viewer. For Java, downloaded
XML is ordered with destinations before their referring elements and the system
root last, as required by the Java loader. IDs and model relationships are preserved. With `--web`, the original XML is
validated and passed unchanged to porisViewer, without reordering. The command
only reads cosmoSys and does not synchronize edits or preserve server UI sessions.
XML is temporary unless `--output FILE` is supplied. Download without launching:

```bash
pyPORIS/poriscsyspanel.sh --no-panel --output /tmp/osiris.xml localhost:3001 osiris
```

Local GraphML synchronization uses the same named configuration:

```bash
pyPORIS/porispanel_csys.sh localhost:3001 --no-panel nrt/mainaxis
pyPORIS/porispanel_dir_csys.sh localhost:3001 --no-panel osiris
# Equivalent direct form:
pyPORIS/porispanel.sh --csys localhost:3001 --no-panel nrt/mainaxis
```

The old Python credential files are not read by these commands. Synchronization
writes to cosmoSys, unlike the remote-panel command. When calling Python importers
directly, set `PORIS_CSYS_INSTANCE` to the configured instance name.

## Shared Python Output Directory

Python products mirror the source directory, without per-model wrapper folders.
For `models/osiris/osiris.graphml` and the `cluster: osi` descriptor in
`models/osiris/cluster.yaml`, the products coexist:

```text
output/py/osiris/osirisPORIS.py
output/py/osiris/osiPORIS.py
```

Regenerating a model replaces only its own generated Python file. Other models
and editable physical companions are preserved. Physical companions live in
`output/py/<source-directory>/<model>_physical/`. GraphML panel commands, the
ODS panel command and the Python generation/run shell commands use this layout.
