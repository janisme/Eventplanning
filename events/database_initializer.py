from events.connect_connector import connect_with_connector


import sqlalchemy
import os

def init_connection_pool() -> sqlalchemy.engine.base.Engine:
    """Sets up connection pool for the app."""
    # use the connector with INSTANCE_CONNECTION_NAME (e.g. project:region:instance)
    if os.environ.get("INSTANCE_CONNECTION_NAME"):
        # Either a DB_USER or a DB_IAM_USER should be defined. here we use db_user
        return connect_with_connector()

    raise ValueError(
        "Missing database connection type. Please define one of INSTANCE_HOST, INSTANCE_UNIX_SOCKET, or INSTANCE_CONNECTION_NAME"
    )

# create 'events' table in database if it does not already exist
def migrate_db(db: sqlalchemy.engine.base.Engine) -> None:
    """Creates the `votes` table if it doesn't exist."""
    with db.connect() as conn:
        pass
        """
        conn.execute(
            sqlalchemy.text(
                "Drop table if exists events_event;"
            )
        )
        """

        conn.execute(
            sqlalchemy.text(
                "CREATE TABLE IF NOT EXISTS events_event "
                "( event_id int auto_increment primary key,"
                " event_title varchar(25),"
                "holder_id varchar(10),"
                "e_date date,"
                "e_detail TINYTEXT,"
                " e_complete boolean default False,"
                #"place varchar(10),"
                #"cat_indoor boolean,"
                "cat_category varchar(10) check ( cat_category in ('Career','Social','Sport','Panel','Unknow')),"
                "capacity int default 50);"
            )
        )
        conn.commit()



#initialize db when run the app
def initialize_database():
    db = init_connection_pool()
    migrate_db(db)
    return db