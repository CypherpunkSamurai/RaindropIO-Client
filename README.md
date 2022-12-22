# RaindropIO-Client

A Raindrop.io WebAPI Client ( It uses login cookies)


## Installation

### Using pip3

To install `raindropio` using `pip3` run the following:
```shell
pip install git+https://github.com/CypherpunkSamurai/RaindropIO-Client.git
```

### Using Git

To install `raindropio` run the following:

```shell
git clone https://github.com/CypherpunkSamurai/RaindropIO-Client.git
cd RaindropIO-Client
python setup.py install
```

## Using the client

Here are examples on how to use the `RaindropIO` client.

```py3
from raindropio import RaindropIO

# extract your cookies after logging in to raindrop.io
# use dev tools
cookies = "your login cookies..."

r = RaindropIO(cookies)

# List all collections
print(r.get_collections())
```

## Credits

- [CypherpunkSamurai](https://github.com/CypherpunkSamurai)

## License

- `MIT`