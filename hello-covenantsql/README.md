# hello-covenantsql

CovenantSQL's "hello world" demo.

## Usage

```bash
./main.py
```

Expected output:

```
$ ./main.py
create table
insert sample data
affected rows: 1, lastrowid: 1
select data from the table
(1, '2018-11-06T18:21:23Z', 'Apple', 'appleisdelicious')

$ ./main.py
create table
insert sample data
affected rows: 1, lastrowid: 2
select data from the table
(1, '2018-11-06T18:21:23Z', 'Apple', 'appleisdelicious')
(2, '2018-11-06T18:21:35Z', 'Apple', 'appleisdelicious')
```

**NB:** you can tweak database configurations through environment variables:

```bash
COVENANTSQL_HOST=192.168.2.xxx COVENANTSQL_PORT=12345 ./main.py
```

Available environment variables are:

- **COVENANTSQL_HOST:** domain of the CovenantSQL adapter service;
- **COVENANTSQL_PORT:** port of the CovenantSQL adapter service;
- **COVENANTSQL_PRIVATE_KEY:** path of the private key file;
- **COVENANTSQL_PROXY_PEM:** path of the proxy pem file;
- **COVENANTSQL_DATABASE:** database name (hash).
