## How To Run (After Cloning)
1. Install `virtualenv`:
```
$ python -m venv .venv
```

2. Then run the command:
```
$ .venv\Scripts\activate
```

3. Then install the dependencies:
```
$ pip install -r requirements.txt
```

3. Select python interpreter (VSCODE):
```
$ ctrl+shift+p
$ select python interpreter (recommended)
```

4. Finally start the web server (run main.py):
```
$ (env) python main.py
```

This server will start on port 5000 by default. You can change this in `main.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
