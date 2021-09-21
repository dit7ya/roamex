from .database import engine
from sqlmodel import Session, select
from .models import Highlight, Page, AnnotationDB
from uuid import UUID
import sqlite3

from pydantic import AnyUrl


org_roam_db_location = "/home/halum/.emacs.d/.local/etc/org-roam.db"

# from sqlmodel import SQLModel, create_engine

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

###########################################################
# Page
###########################################################


def create_page(page: Page):

    with Session(engine) as session:

        session.add(page)
        session.commit()
    return


def read_page(pageUrl: AnyUrl):

    with Session(engine) as session:
        statement = select(Page).where(Page.url == pageUrl)
        try:
            result = session.exec(statement).one()
            return result
        except Exception:
            return {"message": "Page does not exist"}


# Update - NOTE not required
# Delete - NOTE not required

###########################################################
#### Highlights
###########################################################


## Create
def create_highlight(highlight: Highlight):
    with Session(engine) as session:

        session.add(highlight)
        session.commit()


## Read
def read_highlights(pageId: UUID):
    """Return all highlights associated with the pageId."""
    with Session(engine) as session:
        statement = select(Highlight).where(Highlight.pageId == pageId)
        results = session.exec(statement)

        return [x for x in results]


def read_highlight(highlightId: UUID):
    """Return the highlight associated with the given Id."""
    with Session(engine) as session:
        statement = select(Highlight).where(Highlight.id == highlightId)
        result = session.exec(statement).one()

        return result


## Update
## NOTE not required

## Delete
def delete_highlight(id: UUID):

    with Session(engine) as session:
        statement = select(Highlight).where(Highlight.id == id)
        result = session.exec(statement).one()

        session.delete(result)
        session.commit()


###########################################################
#### AnnotationBase
###########################################################


def create_annotation(annotationDb: AnnotationDB):

    with Session(engine) as session:

        session.add(annotationDb)
        session.commit()


def read_annotations(pageId):

    with Session(engine) as session:
        statement = select(AnnotationDB).where(AnnotationDB.pageId == pageId)
        results = session.exec(statement)

        return [r for r in results]


## TODO Update
def update_annotation(id):
    pass


## TODO Delete
def delete_annotation(id):
    pass


def read_org_roam_nodes():
    # TODO REVIEW
    """
    Returns all org-roam nodes stored in its database.
    """
    con = sqlite3.connect(org_roam_db_location)
    cur = con.cursor()

    data = cur.execute("SELECT id, title FROM nodes")

    data_stripped = [
        {"id": row[0].strip('"'), "title": row[1].strip('"')} for row in data
    ]

    if not data:
        con.close()
        return []
    con.close()
    return data_stripped
