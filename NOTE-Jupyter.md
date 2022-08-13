### Lab vs Notebook

jupyter lab is more versatile, jupyter notebook is simpler and straightforward.

**`jupyter lab ...` and `jupyter notebook ...` are mostly alternatively.**

### Basic

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