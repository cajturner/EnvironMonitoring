# HomeTempMonitoring

Simple monitoring system for RaspberryPi environment hat

![](https://media.giphy.com/media/fAT2Db0j0Mblu/giphy.gif)

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

If there is issues installing sense-emu you may need the following:

```bash
export LDFLAGS="-L/usr/local/opt/libffi/lib"
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
```
