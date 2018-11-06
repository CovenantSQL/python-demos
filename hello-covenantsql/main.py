#!/usr/bin/env python3
"""
PyCovenantSQL driver demo: hello-covenantsql
"""

import os
import pycovenantsql

DB_CONFIG = {
    'host':
    os.getenv('COVENANTSQL_HOST', '127.0.0.1'),
    'port':
    int(os.getenv('COVENANTSQL_PORT', '11105')),
    'key':
    os.getenv(
        'COVENANTSQL_PRIVATE_KEY',
        './test/service/node_c/admin.test.covenantsql.io-key.pem',
    ),
    'https_pem':
    os.getenv(
        'COVENANTSQL_PROXY_PEM',
        './test/service/node_c/admin.test.covenantsql.io.pem',
    ),
    'database':
    os.getenv(
        'COVENANTSQL_DATABASE',
        '057e55460f501ad071383c95f691293f2f0a7895988e22593669ceeb52a6452a',
    ),
}


def main():
    """
    Main program
    """

    conn = pycovenantsql.connect(**DB_CONFIG)
    with conn.cursor() as cursor:
        # Create a new table
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS `users` (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `email` VARCHAR(255) NOT NULL,
            `password` VARCHAR(255) NOT NULL
        );
        """
        print('create table')
        cursor.execute(sql_create_table)

        # Insert some data
        print('insert sample data')
        sql_insert_data = """INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"""
        affected_rows = cursor.execute(
            sql_insert_data,
            ('Apple', 'appleisdelicious'),
        )
        print('affected rows: %d, lastrowid: %d' % (
            affected_rows,
            cursor.lastrowid,
        ))

        # Query data
        print('select data from the table')
        sql_select_data = """SELECT * FROM `users`"""
        cursor.execute(sql_select_data)
        for row in cursor:
            print(row)
        conn.close()


if __name__ == '__main__':
    main()
