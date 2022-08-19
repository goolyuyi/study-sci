# iPython

## Introduction

1.

- Comprehensive **object introspection**.
- Extensible **tab completion**, with support by default for completion of python variables and keywords, filenames and
  function keywords.

2.

- Input history, persistent across sessions.

- Caching of output results during a session with automatically generated references.

- Session logging and reloading.
-

3.

- Extensible system of 'magic' commands for controlling the environment and performing many tasks related to IPython or
  the operating system.

- A rich configuration system with easy switching between different setups (simpler than changing `$PYTHONSTARTUP`
  environment variables every time).

- Extensible syntax processing for special purpose situations.

- Access to the system shell with user-extensible alias system.

- Easily embeddable in other Python programs and GUIs.
-

4.

- Integrated access to the pdb debugger and the Python profiler

5.

- real multi-line editing thanks to [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/stable/).

- syntax highlighting as you type.

- integration with command line editor for a better workflow.

6.

- the object to create a rich display of Html, Images, Latex, Sound and Video.

- interactive widgets with the use of the ipywidgets package.

## Manual

### launch

```
> ipython
```

* manually:

```
import os, IPython
os.environ['PYTHONSTARTUP'] = ''  # Prevent running this again
IPython.start_ipython()
raise SystemExit
```

* embed:

```
 >>> __import__("IPython").embed()
 # or
 >>> from IPython import embed; embed()
```

### help system

* `?` - ipython help
* `%quickref`
* `help`
* `object?`

### very useful

* `?np.*ran*` **list all member** contains `ran` in numpy `np`
* `%cd?` get help of `%cd`
* `%pdoc`, `%pdef`, `%psource` and `%pfile`
* `%lsmagic` - list magics
* `<tab>,<S-tab>` - auto complete
* system command:
    * `!ls`,`!vim y.py`
* Put a `;` at the end of a line to suppress the printing of output.
```
In [1]: pyvar = 'Hello world'
In [2]: !echo "A python variable: {pyvar}"
A python variable: Hello world
```

* use `display(obj)` instead of `print(obj)`
    * `from IPython.display import display` for embed

### history

* use `In[1]` `In` `Out[1]` `Out` to retrieve history
* `_` `__` `___`: last three of output
* `%history -n 4-6`
* `_i`,`_ii`,`_iii`: store previous, next previous and next-next previous inputs.
* Additionally, global variables named `_i<n>` are dynamically created (`<n>` being the prompt counter),
  so `_i<n> == _ih[<n>] == In[<n>]`.
* `%rerun` `%macro` to repeat some thing
* `%hist -g somestring` to search history
* `_12`, `Out[12]` or `_oh[12]`
* `%reset` `%xdel` to delete history

### record to .py

* `--logfile=foo.py` or `%logstart`
    * `%logstart [log_name [log_mode]]`
        * `[over:]` overwrite existing log_name.
        * `[backup:]` rename (if exists) to log_name~ and start log_name.
        * `[append:]` well, that says it.
        * `[rotate:]` create rotating logs log_name.1~, log_name.2~, etc.
    * `%logoff` `%logon`

### alias

```
In [1]: %alias parts echo first %s second %s
In [2]: parts A B
```

* where `%s` means param placeholder
* `%rehashx`

### debug

* `%run -d tuts/test.py`

```
In[1]: %run tuts/test-err.py
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
File ~/dev/pythonProjects/study-sci/tuts/test-err.py:8, in <module>
      5 ax = plt.figure().add_subplot(projection='3d')
      6 X, Y, Z = axes3d.get_test_data(0.05)
----> 8 ax.uu()
      9 ax.contour(X, Y, Z, cmap=cm.coolwarm)  # Plot contour curves
     11 plt.show()
In[2]: %debug
```

### misc features

* deep reload - `from IPython.lib.deepreload import reload as dreload`

## Magic

1. `%xxx` line magic `%%xxx` cell magic
2. very useful:

* `%timeit range(1000)`/ `%%timeit x = range(10000) ...`
* `%run y.py` `%run -d y.py`
* `%debug pp(x)`
* `%pushd` `%popd` `%dhist`
* `l=%sx ls`
* `%who`

3. very useful:

- Functions that work with code:[`%run`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-run)
  ,[`%edit`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-edit)
  ,[`%save`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-save)
  ,[`%macro`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-macro)
  ,[`%recall`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-recall), etc.

- Functions which affect the
  shell:[`%colors`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-colors)
  ,[`%xmode`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-xmode)
  ,[`%automagic`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-automagic), etc.

- Other functions such as[`%reset`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-reset)
  ,[`%timeit`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit)
  ,[`%%writefile`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-writefile)
  ,[`%load`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load), or`%paste`.


