from events.models import Event

import sqlalchemy

class eventresource():

    def getlist_all(db: sqlalchemy.engine.base.Engine) -> Event:
        """Retrieves data from the database about the event.
        Args:
            db: Connection to the database.

        Returns:
            A dictionary containing information about votes.
        """
        with db.connect() as conn:
            # Execute the query and fetch all results
            events = conn.execute(
                sqlalchemy.text(
                    "SELECT * FROM events_event"
                )
            ).fetchall()
            print(events)

        return events

    def create(event_title, date, e_detail, capacity, holder_id, cat,
               db: sqlalchemy.engine.base.Engine) -> int:
        stmt = sqlalchemy.text(
            "INSERT INTO events_event (event_title, e_date, capacity, holder_id, e_detail,cat_category,e_complete) "
            "VALUES (:event_title, :e_date, :capacity, :holder_id, :e_detail,:cat_category, False)"
        )
        with db.connect() as conn:
            result = conn.execute(stmt, {"event_title":event_title,
                                         "e_date":date,"capacity":capacity,"holder_id":holder_id,
                                         "e_detail":e_detail, "cat_category":cat })
            conn.commit()
            # Assuming 'event_id' is an auto-incrementing primary key
            inserted_id = result.lastrowid


        return inserted_id

    def get_event( event_id, db: sqlalchemy.engine.base.Engine) -> Event:

        stmt = sqlalchemy.text(
            "SELECT * FROM events_event where event_id = (:id)"
        )

        with db.connect() as conn:
            # Execute the query and fetch all results
            result = conn.execute(
                stmt, {"id": event_id}
            ).fetchone()

        return result

    def delete_event(event_id, db: sqlalchemy.engine.base.Engine) -> Event:
        stmt = sqlalchemy.text(
            "DELETE FROM events_event where event_id = :id"
        )
        id = int(event_id)
        with db.connect() as conn:
            # Execute the query and fetch all results
            result = conn.execute(
                stmt, {"id": id}
            )
            conn.commit()
            print(result)
        return result

    def edit_event(event_id, event_title, date, e_detail, capacity, holder_id, cat,e_complete,
           db: sqlalchemy.engine.base.Engine) -> Event:
        stmt = sqlalchemy.text(
            "UPDATE events_event SET event_title=:event_title, e_date=:e_date, "
            "capacity=:capacity, holder_id=:holder_id, e_detail=:e_detail, "
            "cat_category=:cat_category,e_complete =:e_complete "
            "WHERE event_id=:event_id"
        )
        with db.connect() as conn:
            result = conn.execute(stmt, {
                "event_id": event_id,
                "event_title": event_title,
                "e_date": date,
                "capacity": capacity,
                "holder_id": holder_id,
                "e_detail": e_detail,
                "cat_category": cat,
                "e_complete":e_complete
            })
            #print(result)
            conn.commit()
        return result


