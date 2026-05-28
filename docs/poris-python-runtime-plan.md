# PORIS Python Runtime Plan

## Estado decidido

El XML oficial del flujo de trabajo debe salir del modelo Python generado. El XML directo desde parser queda como herramienta de diagnostico, comparacion y retrocompatibilidad.

Cambio aplicado en `pyPORIS/porispanel.sh`:

- Por defecto genera `output/xml/<ruta>/<modelo>.xml` desde `poris_python2xml.py`.
- El panel Java abre ese XML generado desde Python.
- El XML del parser se genera solo con `--parser-xml` o `--compare-parser`.
- Cuando se activa el parser, su resultado se guarda como `output/xml/<ruta>/<modelo>.from-parser.xml` y se compara contra `output/xml/<ruta>/<modelo>.xml`; el diff queda en `output/xml/<ruta>/<modelo>.xml.diff`.

Comandos previstos:

```bash
pyPORIS/porispanel.sh nrt/mainaxis
pyPORIS/porispanel.sh --parser-xml nrt/mainaxis
pyPORIS/porispanel.sh --compare-parser nrt/mainaxis
```

## Implementacion actual: `pyPORIS/PORIS/PORIS.py`

Es la implementacion viva. Es la que soporta hoy los modelos generados y el XML desde Python.

Fortalezas:

- Tiene `PORISDoc`, gestion de raiz, asignacion de IDs y exportacion/importacion XML completa.
- Implementa reglas de seleccion de modos y valores que ya estan siendo usadas por los modelos generados.
- Tiene formatters reales: double, integer, date, HMS, DMS, arcmin, arcsec.
- Ya integra `PORISCmd` con ejecucion, callback y override en `physical`.
- Es compatible con el generador actual.

Debilidades:

- Es monolitica: unas 100 KB en un solo fichero.
- Mezcla runtime de configuracion, XML, formatters, documento y utilidades de carga.
- Usa varios patrones heredados, como mutar `__class__` durante `fromXML`.
- No esta separada por perfiles: desktop/full, runtime sin XML, micropython, etc.
- La estructura de relaciones esta repartida entre diccionarios especializados (`modes`, `params`, `subsystems`, `commands`) y metodos de destino XML.

Conclusion: debe seguir siendo la base funcional de corto plazo. No conviene sustituirla de golpe.

## Implementacion MVC: `pyPORIS/PORIS/MVC`

La implementacion MVC parece conceptualmente mas limpia: parte de `Model`, `Observer`, `Controller`, `View`, relaciones source/destination genericas, y una libreria `PORISLib` como contenedor.

Fortalezas conceptuales:

- Tiene separacion de responsabilidades: modelo observable, vistas/controladores, libreria de nodos.
- Usa una relacion generica `sources/destinations`, que puede simplificar XML, navegacion y validaciones.
- Apunta a un PORIS mas extensible para UI y sincronizacion.
- La estructura por ficheros facilita mantener el runtime.

Problemas encontrados:

- No es ejecutable como sustituto actual.
- `testPORIS.py` hereda de `PORISDoc`, pero MVC no define `PORISDoc`.
- Hay importaciones circulares entre `PORISNode`, `PORISMode` y `PORISValue`.
- `PORISValueFloat.py` usa genericos como `PORISValueDataRange[T]` sin una base compatible en runtime.
- Hay errores tipograficos o APIs tipo Java no traducidas: `señf`, `chilNodes`, `getNodeName`, `getTextContent`, `setNodeValue`, `_xmlLoaderHashMap`.
- Algunas firmas no coinciden entre clases, por ejemplo `toXML(doc, tagClass, onlyIdent)` frente a `toXML(doc, onlyIdent)`.
- `PORISNode.getModes()` intenta acceder a `self.__destinations`, que es privado de `PORIS` y no visible desde la subclase.

Comprobaciones realizadas:

```bash
python3 -m py_compile pyPORIS/PORIS/MVC/*.py
PYTHONPATH=pyPORIS/PORIS/MVC python3 -c 'import testPORIS'
PYTHONPATH=pyPORIS/PORIS/MVC python3 -c 'import PORISNode'
PYTHONPATH=pyPORIS/PORIS/MVC python3 -c 'import PORISValueFloat'
```

Resultado: compila, pero falla al importar modulos clave.

Conclusion: MVC es una buena referencia arquitectonica, pero no una base lista para reemplazar `PORIS.py`. La estrategia buena es extraer sus ideas y migrar incrementalmente.

## Objetivo: una unica implementacion PORIS

Propuesta de destino:

- Un paquete unico, por ejemplo `pyPORIS/PORIS/runtime/`.
- API publica compatible con los nombres actuales: `PORISDoc`, `PORIS`, `PORISNode`, `PORISSys`, `PORISParam`, `PORISMode`, `PORISValue`, `PORISValueFloat`, `PORISValueString`, `PORISCmd`.
- Internamente, usar relaciones genericas tipo MVC: cada nodo conoce `destinations` y `sources`.
- Mantener fachadas especializadas (`addMode`, `addParam`, `addSubsystem`, `addCommand`, `addValue`) para compatibilidad y claridad.
- Separar capacidades en modulos:
  - `core.py`: nodos, relaciones, seleccion.
  - `document.py`: `PORISDoc`, raiz, IDs, coleccion.
  - `values.py`: valores y datos.
  - `commands.py`: comandos/callbacks.
  - `formatters.py`: formatters.
  - `xmlio.py`: import/export XML.
  - `observable.py`: opcional, inspirado en MVC.

Compatibilidad necesaria:

- Los modelos generados actuales deben seguir importando `from PORIS import *`.
- Puede mantenerse un `PORIS.py` fino que reexporte el paquete nuevo.
- Los `physical` no deben necesitar manipular `PYTHONPATH`; eso corresponde a `runPorisModel.sh`.

## MicroPython / `savemem`

El modo reducido existe parcialmente como `config.savemem`.

Donde esta:

- `pyPORIS/config.py`: `savemem = False`
- `pyPORIS/poris_codegen.py`: ramas `if not savemem` / `else`
- `pyPORIS/testExamplePORIS_savemem.py`: prueba antigua de ese perfil

Que hace hoy:

- Reduce algunos nombres de instancia.
- Omite metadatos como `ident`, `setXMLName()` y `description`.
- Cambia parte de las relaciones generadas a nombres mas cortos.

Que no hace hoy:

- No tiene flag de linea de comandos.
- No genera una copia reducida del runtime PORIS.
- No elimina import/export XML de forma estructural.
- No elimina comentarios de forma sistematica.
- No produce un paquete autosuficiente para MicroPython.
- Algunas ramas `savemem` parecen inconsistentes y deben probarse antes de darlas por validas.

Propuesta de perfiles:

```text
full
  Runtime completo con XML, formatters, labels, attributes, commands, callbacks.

runtime
  Sin XML ni parser; conserva seleccion, valores y comandos.

micro
  Runtime minimo para MicroPython: sin XML, sin minidom, sin datetime pesada si no hace falta,
  sin observer, sin labels/attributes/descriptions, nombres compactos opcionales.
```

CLI propuesta:

```bash
pyPORIS/doPorisPython.sh --profile full example/example
pyPORIS/doPorisPython.sh --profile runtime example/example
pyPORIS/doPorisPython.sh --profile micro example/example
```

Productos propuestos:

```text
output/py/<modelo>/<modelo>/<modelo>PORIS.py
output/py/<modelo>/<modelo>_physical/<modelo>_physical.py
output/py/<modelo>/<modelo>_micro/PORIS.py
output/py/<modelo>/<modelo>_micro/<modelo>PORIS.py
```

En `micro`, el modelo deberia importar el runtime local reducido:

```python
from PORIS import *
```

Asi el bundle se puede copiar entero a una placa sin depender del submodulo.

## Plan incremental

1. Cerrar el flujo XML desde Python.
   - Hecho para `porispanel.sh`.
   - Falta decidir si migrar tambien scripts antiguos: `porispanel_dir.sh`, `porispanel_csys.sh`, `porispanel_dir_csys.sh`, `odsporispanel.sh`.

2. Estabilizar una suite de equivalencia.
   - Para cada modelo: generar Python, XML desde Python, opcional XML parser.
   - Abrir panel con XML Python.
   - Validar root, nombres visibles, comandos, IDs internos y roundtrip XML.

3. Extraer un nucleo PORIS limpio desde `PORIS.py`.
   - Primero sin cambiar API publica.
   - Mantener `PORIS.py` como fachada de reexport.
   - Cubrir con tests de `example`, `mainaxis`, `ARCGenIII`, `osiris`.

4. Reincorporar ideas MVC con cuidado.
   - Observable opcional, no obligatorio para MicroPython.
   - `sources/destinations` como relacion canonica.
   - `PORISLib` o `PORISDoc` como contenedor unico, probablemente conservando el nombre `PORISDoc`.

5. Convertir `savemem` en perfiles reales.
   - Anadir `--profile`.
   - Pasar configuracion al generador en vez de depender solo de `config.savemem`.
   - Corregir ramas `savemem`.
   - Generar runtime reducido.

6. Crear runtime MicroPython.
   - Sin `xml.dom.minidom`.
   - Sin import/export.
   - Sin formatters no necesarios.
   - Con seleccion de modos/valores, valores numericos/string y comandos.
   - Con callback/override de comandos si aporta valor en dispositivo.

7. Retirar duplicados.
   - Una sola implementacion fuente.
   - Un runtime full generado/importable.
   - Un runtime micro derivado o escrito como subconjunto mantenido.

## Recomendacion

No migraria directamente a MVC. Usaria `PORIS.py` como verdad funcional y moveria su contenido hacia una arquitectura modular que adopte las buenas ideas de MVC. Despues de eso, `MVC/` puede convertirse en referencia historica o eliminarse.

Para MicroPython, no intentaria "minificar" el runtime full. Es mejor generar un runtime pequeno por perfil, con una API comun minima, y que el generador sepa emitir el modelo contra esa API.
