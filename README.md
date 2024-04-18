# hacknuthon

HackNUThon 2024.


### Development Environment Setup

1. Install [python](https://python.org), [poetry](https://python-poetry.org/), [mysql](https://www.mysql.com/products/community/) (make sure `mysql` is on PATH) and (optionally) [stella](https://github.com/shravanasati/stellapy) on your system.

2. Clone the repository (fork first if you want to contribute).

```sh
git clone https://github.com/shravanasati/hacknuthon.git
```

Change the github username in the above URL if you have forked the repository.

3. Create a virtual environment (strongly recommended). 

```sh
python -m venv venv
```

And activate it.

On Windows powershell
```powershell
./venv/Scripts/Activate.ps1
```

On unix based systems
```sh
source ./venv/bin/activate
```

4. Install all the dependencies.

```sh
poetry install --no-root
```

5. Run the server.

```sh
flask --app app run
```

If you've installed stella, you can get live reloading capabilities for both backend and frontend.

```sh
stella run server
```
for just running the server.

```sh
stella run
```
for running the server as well as having reload on browser.

```sh
stella run serve-all
```
to serve on all interfaces (i.e., to view the website on a mobile on the same network)