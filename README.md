# python-sanlock

Python bindings for the [sanlock](https://pagure.io/sanlock) library.

Originally developed as part of the sanlock project and used by oVirt/vdsm,
this package is now maintained as a standalone module.

## Requirements

### Runtime

- sanlock >= 5.0.0 (`sanlock-lib` package on RHEL/Fedora)

### Build

- Python >= 3.6
- gcc
- sanlock development headers (`sanlock-devel` on RHEL/Fedora)

On RHEL/Fedora:

```sh
dnf install gcc python3-devel sanlock-devel
```


## Installation

```sh
pip install sanlock-python
```

Or from source:

```sh
pip install .
```

## Usage

```python
import sanlock

# Register with the sanlock daemon
fd = sanlock.register()

# Write a lockspace
sanlock.write_lockspace(b"my_lockspace", "/path/to/disk", iotimeout=10)

# Add the lockspace (acquire host_id)
sanlock.add_lockspace(b"my_lockspace", 1, "/path/to/disk")

# Write a resource
sanlock.write_resource(b"my_lockspace", b"my_resource", [("/path/to/disk", 0)])

# Acquire the resource
sanlock.acquire(b"my_lockspace", b"my_resource", [("/path/to/disk", 0)], slkfd=fd)

# Release the resource
sanlock.release(b"my_lockspace", b"my_resource", [("/path/to/disk", 0)], slkfd=fd)

# Remove the lockspace
sanlock.rem_lockspace(b"my_lockspace", 1, "/path/to/disk")
```

See `example.py` for a more complete example.

## Testing

Tests require a running sanlock daemon and the `pytest` framework.

```sh
# Install test dependencies
pip install pytest userstorage

# Set up the environment
source tests/env.sh

# Run the tests
pytest tests/
```

To enable 4K sector tests, set up userstorage first:

```sh
userstorage create tests/storage.py
pytest tests/
userstorage delete tests/storage.py
```

## License

GPL-2.0-or-later — see `COPYING`.
