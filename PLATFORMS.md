# Installing ChumpMan11D

## Linux

```
git clone https://github.com/zklaas/chumpman11d.git
cd chumpman11d
python3 -m pip install --user PyQt6 PyQt6-WebEngine   # or your distribution's packages
./install.sh

# or, without installing: open game.html in a web browser (from https://github.com/zklaas/chumpman11d)
```

## Windows (untested)

```
git clone https://github.com/zklaas/chumpman11d.git
cd chumpman11d
py -m pip install PyQt6 PyQt6-WebEngine
powershell -ExecutionPolicy Bypass -File install.ps1

# or, without installing: open game.html in a web browser (from https://github.com/zklaas/chumpman11d)
```

## macOS (untested)

```
git clone https://github.com/zklaas/chumpman11d.git
cd chumpman11d
python3 -m pip install --user PyQt6 PyQt6-WebEngine
python3 chumpman11d.py

# or, without installing: open game.html in a web browser (from https://github.com/zklaas/chumpman11d)
```
