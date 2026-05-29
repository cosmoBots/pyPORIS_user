# PORIS Generation Validation

Fecha: 2026-05-28

## Cambio de flujo

Los comandos de panel/generacion Linux quedan orientados a XML desde Python:

- `pyPORIS/porispanel.sh`
- `pyPORIS/porispanel_dir.sh`
- `pyPORIS/porispanel_csys.sh`
- `pyPORIS/porispanel_dir_csys.sh`
- `pyPORIS/odsporispanel.sh`
- `pyPORIS/winporispanel.bat`

El producto principal es:

```text
output/xml/<ruta>/<modelo>.xml
```

Ese XML se genera instanciando el modelo Python y llamando a `toXML()`.

El XML directo desde parser ya no es el producto principal. Si hace falta compararlo:

```bash
pyPORIS/porispanel.sh --parser-xml --no-panel nrt/mainaxis
pyPORIS/porispanel.sh --dir --parser-xml --no-panel osiris
```

En ese caso se genera:

```text
output/xml/<ruta>/<modelo>.from-parser.xml
output/xml/<ruta>/<modelo>.xml.diff
```

## Modelos ejecutados

Se ejecuto el flujo real de `porispanel.sh --no-panel --parser-xml` sobre:

- `ARCGenIII`
- `osiris`
- `example/a`
- `example/b`
- `example/c`
- `example/example`
- `example/example_evolved`
- `example/simple`
- `nrt/mainaxis`

## Resultado estructural

| Modelo | Parser | Python | Diferencia relevante |
| --- | ---: | ---: | --- |
| `ARCGenIII` | 118 | 109 | Python elimina 13 `VIRT-*` y anade 4 `PORISCmd` |
| `osiris` | 413 | 405 | Python elimina 10 `VIRT-*` y anade 2 `PORISCmd` |
| `example/a` | 5 | 5 | Sin perdida real |
| `example/b` | 5 | 3 | Python elimina 2 `VIRT-*` |
| `example/c` | 15 | 14 | Python elimina 1 `VIRT-*` |
| `example/example` | 47 | 47 | Sin perdida real |
| `example/example_evolved` | 71 | 70 | Python elimina 1 `VIRT-*` |
| `example/simple` | 34 | 34 | Sin perdida real |
| `nrt/mainaxis` | 35 | 34 | Python elimina 1 `VIRT-*` |

En todos los modelos analizados:

- `missing_real = 0`: no desaparece ningun nodo con identificador real, ignorando `VIRT-*` y `ENG-*`.
- Los comandos aparecen solo en Python, que es el comportamiento deseado:
  - `ARCGenIII`: `expose`, `init_expose`, `cfg_init_expose`, `abort`
  - `osiris`: `acquire`, `abort`
- Las diferencias de `ENG-*` son renumeraciones internas de modos Engineering.
- Las diferencias de nombres como `0_6` frente a `0.6`, `Range2_0` frente a `Range2.0`, o `Calibracion` frente a `Calibración` son mejoras de fidelidad del XML Python respecto al texto original del modelo.

## Lectura

Los cambios van en el buen sentido. El XML Python conserva los nodos reales, evita nodos virtuales redundantes del parser, preserva mejor los nombres visibles y representa comandos como nodos ejecutables.

No se ha detectado regresion estructural en los modelos ejecutados.

## Pendientes

- Decidir si se eliminan del repositorio los productos antiguos `*.from-python.xml`; el nuevo nombre principal es `*.xml`.
- Decidir si los XML antiguos en rutas historicas como `output/xml/osiris/osiris.xml` u `output/xml/ARCGenIII/ARCGenIII.xml` deben migrarse o eliminarse.
- Verificar `winporispanel.bat` en Windows. Se ha actualizado al flujo Python, pero no se ha ejecutado en esta maquina.
