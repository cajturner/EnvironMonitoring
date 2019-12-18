# HomeTempMonitoring

## Run

```bash
docker-compose up
pipenv shell
python src/Sensor.py
```

## Develop

```bash
pipenv shell
pipenv install
python src/Sensor.py
```

export LDFLAGS="-L/usr/local/opt/libffi/lib"

For pkg-config to find libffi you may need to set:
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
