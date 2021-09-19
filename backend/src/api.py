#!/usr/bin/env python3
from src import dbops

# import fileops
from uuid import UUID

from pydantic import AnyUrl

from .database import create_db_and_tables
from .models import Page, Highlight, AnnotationBase, Annotation, AnnotationDB
from fastapi import FastAPI, Response, status


# create_db_and_tables()  # TODO Look at me

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


###########################################################
#### Page
###########################################################

## Create
@app.post("/pages", status_code=201)
def create_page(page: Page):

    # dbops
    dbops.create_page(page)

    # fileops
    # fileops.create_page(page)

    return {"message": "Page created."}


## Read
@app.get("/pages/")
def read_page(url: AnyUrl):

    # dbops
    page = dbops.read_page(url)

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
@app.get("/highlights/")
def read_highlights(pageUrl: AnyUrl):

    highlights = dbops.read_highlights(pageUrl)

    return highlights


## Update - NOTE Not Required

## Delete
@app.delete("/highlights/{id}")
def delete_highlight(id: UUID):

    # dbops
    dbops.delete_highlight(id)
    # fileops
    # fileops.delete_highlight(id)

    return {"message": "Highlight deleted."}


###########################################################
#### AnnotationBase
###########################################################


## Create
@app.post("/annotations", status_code=201)
def create_annotation(annotation: Annotation):

    annotationDb = AnnotationDB(
        id=annotation.id,
        orgId=annotation.orgId,
        highlightId=annotation.highlightId,
        pageUrl=annotation.pageUrl,
    )

    # dbops
    dbops.create_annotation(annotationDb)

    # fileops
    # fileops.create_annotation(annotation)

    return {"message": "Annotation created."}


## Read
@app.get("/annotations/{pageUrl}")
def read_annotations(pageUrl: AnyUrl):

    # dbops
    annotations = dbops.read_annotations(pageUrl)
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
