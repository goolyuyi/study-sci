## Lab vs Notebook

jupyter lab is more versatile, jupyter notebook is simpler and straightforward.

**`jupyter lab ...` and `jupyter notebook ...` are mostly alternatively.**

## Jupyter Notebook Basic

run locally

```
jupyter notebook 
jupyter notebook --notebook-dir=.
```

* args:
    * `--notebook-dir`: (work dir)directory to store notebooks
    * `--port 9999`: port number
    * `notebook.ipynb` open specific file
    * `--no-browser` do not open browser
    * `--allow-errors`

### Config

* Config files are stored by default in the `~/.jupyter` directory.
    * env var `JUPYTER_CONFIG_DIR` `JUPYTER_CONFIG_PATH`
    * `jupyter --paths`
    * `jupyter --config-dir`
* Data path(e.g. plugin data):
    * env var `JUPYTER_DATA_DIR`
    * `jupyter --data-dir`
* Runtime path
    * env var `JUPYTER_RUNTIME_DIR`
    * `jupyter --runtime-dir`

## Jupyter Lab Basic

### run with working dir

```
jupyter lab ./
```

args:

* `--show-config`
* `--generate-config`
* `--no-browser`
* `--autoreload`
* `--core-mode` `--dev-mode`
* `--watch`
* `--port` `--ip`
* `--app-dir=`

### jupyter lab session always with workspace, default is `/Lab`

* lab include classic notebook:
    * `http://localhost:8888/lab` lab
    * `http://localhost:8888/tree` notebook view

### jupyter kernel:

* https://www.wrighters.io/connecting-to-your-notebook-kernel-using-jupyter-console/
    * `jupyter console --existing`
    * `%connect_info` magic method

### url

* `/lab/tree`: `http://localhost:8888/lab/tree/tuts/3-jupyter-ipython.ipynb`

workspace:

* default work space: `http://localhost:8888/lab/`
* `/workspaces/named`: `http://localhost:8888/lab/workspaces/debug`
* workspace can share
* > A workspace should only be open in a single browser tab at a time. If JupyterLab detects that a workspace is being
  opened multiple times simultaneously, it will prompt for a new workspace name.
* reset workspace: `http://localhost:8888/lab/workspaces/debug`
* clone

### extension

* extension is a npm package not a python package!
* `jupyter labextension install my-extension my-other-extension`
* `jupyter labextension uninstall my-extension my-other-extension`
* manually rebuild: `--no-build`->`jupyter lab build`
* `jupyter labextension list`
* `jupyter labextension disable my-extension`
* `jupyter labextension enable my-extension`
* more: https://jupyterlab.readthedocs.io/en/stable/user/extensions.html

### path

* show path: `jupyter lab path` / `jupyter --paths`
    * Application Directory: where JupyterLab stores the main build of JupyterLab with associated data, including
      extensions built into JupyterLab.
        * The application directory can be overridden using the --app-dir command-line option in any of the JupyterLab
          commands, or by setting the JUPYTERLAB_DIR environment variable.
    * User Settings Directory: where JupyterLab stores user-level settings for JupyterLab extensions
    * Workspaces Directory: where JupyterLab stores workspaces
