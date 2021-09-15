#!/usr/bin/env python3
from src import dbops

# import fileops
from uuid import UUID

# from .database import create_db_and_tables
from .models import Page, Highlight, AnnotationBase
from fastapi import FastAPI, Response, status

# from sqlmodel import Session


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


# create_db_and_tables()  # TODO Look at me
#
#
#

app = FastAPI()

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


# session = get_session()


###########################################################
#### Page
###########################################################

## Create
@app.post("/page", status_code=201)
def create_page(page: Page):

    # dbops
    # dbops.create_page(page)

    # fileops
    # fileops.create_page(page)

    return {"message": "Page created."}


## Read
@app.get("/pages/{pageId}")
def read_page(pageId: UUID):

    # dbops
    # page = dbops.read_page(pageId)

    # FIXME fileops

    return page


## Update - NOTE Not Required
## Delete - NOTE Not Required

###########################################################
#### Highlight
###########################################################

## Create
@app.post("/highlights", status_code=201)
def create_highlight(highlight: Highlight):

    # dbops
    dbops.create_highlight(highlight)

    # fileops
    # fileops.create_highlight(highlight)

    return {"message": "Highlight created."}


## Read
@app.get("/highlights/{pageId}")
def read_highlights(pageId: UUID):

    # print("hello")
    # dbops
    highlights = dbops.read_highlights(pageId)
    print(highlights)

    return highlights


## Update - NOTE Not Required

## Delete
@app.delete("/highlights/{id}")
def delete_highlight(id: UUID):

    # dbops
    # dbops.delete_highlight(id)
    # fileops
    # fileops.delete_highlight(id)

    return {"message": "Highlight deleted."}


###########################################################
#### AnnotationBase
###########################################################


## Create
@app.post("/annotations", status_code=201)
def create_annotation(annotation: AnnotationBase):

    # dbops
    # dbops.create_annotation(annotation)

    # fileops
    # fileops.create_annotation(annotation)

    return {"message": "Annotation created."}


## Read
@app.get("/annotations/{highlightId}")
def read_annotations(highlightId: UUID):

    # dbops
    # annotations = dbops.read_annotations(highlightId)

    # FIXME fileops

    return annotations


## Update
@app.put("/annotations/{id}")
def update_annotation(id: UUID):

    # dbops
    # dbops.update_annotation(id)
    # fileops
    # fileops.update_annotation(id)

    return {"message": "Annotation updated."}


## Delete
@app.delete("/annotation/{id}")
def delete_annotation(id: UUID):

    # dbops
    # dbops.delete_annotation(id)
    # fileops
    # fileops.delete_annotation(id)

    return {"message": "Annotation deleted."}
