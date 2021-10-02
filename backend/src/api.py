from src import dbops
from src import fileops

# import fileops
from uuid import UUID

from pydantic import AnyUrl

from .database import create_db_and_tables
from .models import (
    Page,
    Highlight,
    Annotation,
    AnnotationDB,
    PageBase,
    PageDB,
    PageComment,
)
from fastapi import FastAPI, Response, status

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    fileops.create_roamex_directory()


###########################################################
#### Page
###########################################################

## Create
@app.post("/pages", status_code=201)
def create_page(page: Page):

    pageDb = PageDB(
        url=page.url,
        title=page.title,
        id=page.id,
    )

    # fileops
    fileops.create_page(page)

    # REVIEW Fileops must be run first cause once dbops uses the
    # page object in its session it is no longer available

    # dbops
    dbops.create_page(pageDb)

    return {"message": "Page created."}


## Read
@app.get("/pages")
def read_page(url: AnyUrl):

    # dbops
    pageDb = dbops.read_page(url)

    # TODO add pageComment too

    return pageDb


@app.put("/pages/{pageId}")
def update_page(pageId: UUID, pageComment: PageComment):

    # REVIEW
    fileops.update_page_comment(pageId, pageComment.text)
    return {"message": "Page comment updated."}


## Update - NOTE Not Required
## Delete - NOTE Not Required

###########################################################
#### Highlight
###########################################################

## Create
@app.post("/highlights", status_code=201)
def create_highlight(highlight: Highlight):

    # fileops
    fileops.create_highlight(highlight)
    # dbops
    #
    # print(highlight)
    dbops.create_highlight(highlight)

    return {"message": "Highlight created."}


## Read
@app.get("/highlights/{pageId}")
def read_highlights(pageId: UUID):

    print(pageId)
    highlights = dbops.read_highlights(pageId)

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
        # orgId=annotation.orgId, // TODO FIXME
        highlightId=annotation.highlightId,
        pageId=annotation.pageId,
    )

    # fileops
    fileops.create_annotation(annotation)

    # dbops
    dbops.create_annotation(annotationDb)

    return {"message": "Annotation created."}


## Read
@app.get("/annotations/{url}")
def read_annotations(url: AnyUrl):

    # dbops
    annotations = dbops.read_annotations(url)
    # TODO fileops

    return annotations


## Update TODO
@app.put("/annotations/{id}")
def update_annotation(id: UUID):

    # dbops
    # dbops.update_annotation(id)
    # fileops
    # fileops.update_annotation(id)

    return {"message": "Annotation updated."}


## Delete TODO
@app.delete("/annotations/{id}")
def delete_annotation(id: UUID):

    # dbops
    # dbops.delete_annotation(id)
    # fileops
    # fileops.delete_annotation(id)

    return {"message": "Annotation deleted."}


@app.get("/orgRoamNodes")
def read_org_roam_nodes():
    org_roam_nodes = dbops.read_org_roam_nodes()

    return org_roam_nodes
