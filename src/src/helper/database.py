import pymysql


def database_connection():
    try:
        host = 'fasttrackacademygui.c6hbqgzgindj.us-west-2.rds.amazonaws.com'
        user = 'admin'
        passwd = 'fast_track_academy'
        db = 'fast_track_academy'

        return pymysql.connect(host=host, user=user, passwd=passwd, db=db)
    except Exception as exception:
        print(exception)
        return None


class connect:

    def exec(mysql):
        connection = database_connection()
        if connection:
            cursor = connection.cursor()

            def exec_string(command):
                try:
                    cursor.execute(command)
                    connection.commit()
                    return True
                except Exception as exception:
                    print("execution fails")
                    print(exception)
                    connection.rollback()
                    return False
            if isinstance(mysql,list):
                for string in mysql:
                    print(string)
                    execute = exec_string(string)
                    if not execute:
                        return False
                return True
            else:
                return exec_string(mysql)
        else:
            return False

    def get_data(mysql):
        connection = database_connection()
        if connection is not None:
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            try:
                cursor.execute(mysql)
                return cursor.fetchall()
            except Exception as exception:
                return None
        else:
            return None