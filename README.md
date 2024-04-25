# hacknuthon

HackNUThon 2024.

## System idea
![image](https://github.com/shravanasati/hacknuthon-24/blob/master/static/images/fun.png)

### Development Environment Setup

1. Install [python](https://python.org), [poetry](https://python-poetry.org/), [nodejs](https://nodejs.org/en/download), [mysql](https://www.mysql.com/products/community/) (make sure `mysql` is on PATH) and (optionally) [stella](https://github.com/shravanasati/stellapy) on your system.

2. Clone the repository (fork first if you want to contribute).

```sh
git clone https://github.com/shravanasati/hacknuthon-24.git
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

To install all the python dependencies:

```sh
poetry install --no-root
```

To install all the npm dependencies:

```sh
npm i
```


<!-- 5. Setup the database.

Login into MySQL using the command:

```sh
mysql -u {username} -p
```

Create the `hacknuthon` database:

```sh
create database hacknuthon;
```

Now, go the project base and add a file named with `.env` with the following content:

```
MYSQL_USERNAME={username}
MYSQL_PASSWORD={password}
MYSQL_HOST=localhost
MYSQL_PORT=3306
DB_POOL_SIZE=50
DB_POOL_RECYCLE=1800
```

The host and port arguments here are the default ones. If your MySQL server runs on a different host and port, modify them accordingly. The `DB_POOL_SIZE` indicates the size of connection pool used my SQLAlchemy. The `DB_POOL_RECYCLE` value indicates the duration in seconds after which the connection should be recycled

(don't include curly braces in the file) -->

5. More configurations.

Another configuration you'd need to be able to run the server is `SECRET_KEY`, which is used by login manager to keep client-side sessions secure.

Generate a safe secret key using python:

```sh
python -c "import secrets;print(secrets.token_hex(64))"
```

Set the value as follows, in the `.env` file:

```
SECRET_KEY={secret_key}
```

6. Run the server.

Open 3 terminal sessions and execute following commands in the respective session:

- Session 1

```sh
npm run tailwind
```

This will enable the tailwind watcher that detects changes in tailwind css.

- Session 2

```sh
npm run webpack
```

This will enable the webpack watcher to bundle javascript.

- Session 3

**Always** execute python-related commands inside an activated virtual environment.

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

to serve on all interfaces (i.e., to view the website on a mobile on the same network).

> **ALWAYS** use `ex` command to stop stella, **don't use `CTRL + C`**.
