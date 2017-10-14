# Hinweise

Das Verzeichnis `05-generate-docs` ist ein Beispiel für die automatische Erzeugung von Software-Dokumentation auf Basis von docstrings im Quellcode.

Das Verzeichnis `fsfw_demo_package` enthält den zu dokumentierenden Beispiel-Code.

Der Inhalt des Verzeichnisses `doc` wurde ein mehreren Schritten erzeugt.
1. Ausführung von `sphinx-quickstart`. Dabei werden interaktiv einige Parameter abgefragt. Für die Reproduzierbarkeit ist hier das Ergebnis weiter unten festgehalten.
2. Anpassung von `doc/source/conf.py`, sodass das zu dokumentierende Python-Paket `fsfw_demo_package` gefunden wird
3. Ausführung von `sphinx-apidoc -f -o doc/source fsfw_demo_package/`. Dadurch werden relevante Dateien im Verzeichnis `doc/source` erzeugt.
4. Anpassung von `doc/source/index.rst` zur Einbindung dieser Dateien, sowie von intro.rst (manuell erstellt).
5. Ausführung von `make html` im Verzeichnis `doc`. Dadurch wird in `doc/build` die HTML-Dokumentation erzeugt (Ergebnis: siehe `doc/build/html/index.html`). Der Befehl `make html` ist am besten zweimal hintereinander auszuführen.

Der genaue Inhalt der manuell geänderten Dateien lässt sich z.B. mit folgenden Befehlen anzeigen:
* `kdiff3 conf.py_original conf.py`
* `kdiff3 index.rst_original index.rst`

Mehr Informationen zur Doku-Erzeugung sind z.B. im [Sphinx Tutorial](http://www.sphinx-doc.org/en/stable/tutorial.html) verfügbar.


## Aus- und Eingabe für sphinx-quickstart

    Welcome to the Sphinx 1.6.3 quickstart utility.

    ...

    Enter the root path for documentation.
    > Root path for the documentation [.]: doc

    ...

    > Separate source and build directories (y/n) [n]: y

    ...

    > Name prefix for templates and static dir [_]:

    ...

    > Project name: hello-world-autodoc-example
    > Author name(s): FSFW Dresden

    ...

    > Project version []: 1.0
    > Project release [1.0]:

    ...

    > Project language [en]:

    ...

    > Source file suffix [.rst]:

    ...

    > Name of your master document (without suffix) [index]:

    ...

    > Do you want to use the epub builder (y/n) [n]:

    ...

    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    > doctest: automatically test code snippets in doctest blocks (y/n) [n]:
    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y

    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: n
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
    > viewcode: include links to the source code of documented Python objects (y/n) [n]: n
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n

    ...

    > Create Makefile? (y/n) [y]:
    > Create Windows command file? (y/n) [y]:

    Creating file doc/source/conf.py.
    Creating file doc/source/index.rst.
    Creating file doc/Makefile.
    Creating file doc/make.bat.

    Finished: An initial directory structure has been created.

