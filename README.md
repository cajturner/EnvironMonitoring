# HomeTempMonitoring

ssh pi@109.146.71.125

## Develop

```bash
pipenv shell
python src/Sensor.py

```

export LDFLAGS="-L/usr/local/opt/libffi/lib"

For pkg-config to find libffi you may need to set:
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
