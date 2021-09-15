from .database import engine
from sqlmodel import Session, select
from .models import Highlight, AnnotationBase, Page
from uuid import UUID


# from sqlmodel import SQLModel, create_engine

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

###########################################################
#### Page
###########################################################

## TODO Create
def create_page(page: Page):
    pass


## TODO Read
def read_page(pageId: UUID):
    pass


## Update - NOTE not required
## Delete - NOTE not required

###########################################################
#### Highlights
###########################################################


## Create
def create_highlight(highlight: Highlight):
    with Session(engine) as session:

        statement = select(Highlight).where(
            Highlight.pageId == "ff7bd2f4-d143-4820-ab6c-5f5cc91e8e86"
        )

        results = session.exec(statement)
        for r in results:
            print(r)
        session.add(highlight)
        session.commit()


## Read
def read_highlights(pageId: UUID):
    """Return all highlights associated with the pageId."""
    # print(pageId)
    # session = get_session()
    with Session(engine) as session:
        statement = select(Highlight).where(Highlight.pageId == pageId)
        # statement = select(Highlight)

        # statement = select(Highlight).where(
        #     Highlight.pageId == "ff7bd2f4-d143-4820-ab6c-5f5cc91e8e86"
        # )
        # print(statement)
        results = session.exec(statement)
        # print(type(results))
        # for r in results:
        #     print(r)

        return [x for x in results]


## Update
## NOTE not required

## Delete
def delete_highlight(id: UUID):
    pass


###########################################################
#### AnnotationBase
###########################################################

## TODO Create
def create_annotation(annotation: AnnotationBase):
    pass


## TODO Read
def read_annotations(highlightId):
    pass


## TODO Update
def update_annotation(id):
    pass


## TODO Delete
def delete_annotation(id):
    pass
