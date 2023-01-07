# Callback

An ultra simple callback gateway for executing command on host


## Usage

1. Create a folder named `plugin`
2. For each plugin, it has a unique name of folder in that folder
3. This gateway will call `main.sh` or `main.py` (if it exists) when getting requests
4. This project is realy simple that it can **only** be used under security-insensitive circumstance (But u can modify it)

## Call method

> The default token can be changed on `model.py`
> 
> For further authoritative methods, you can modify by yourself

Provided there is a plugin named `plugin.example.main` that contains:

```python
from model import BasePlugin

class Plugin(BasePlugin):
    def run(self, param) -> str:
        print('Hello world from python!')
        return 'Hello world'
```

and a bash file named `plugin/example/bash.sh` that contains:

```bash
echo Hello world from bash
```

and we run the server:

```bash
python3 main.py
# or
bash run.sh  # Will run in background and output log to this.log
```

Now, we can call this plugin using:

```
curl -X POST 127.0.0.1:8000/example -d '{"token": "default_token"}'
```

and we can see the result.
