"""This module defines the data models and API schema."""

from sqlmodel import Field, SQLModel
from pydantic import AnyUrl
from uuid import UUID
from typing import Optional


class Highlight(SQLModel, table=True):
    """Highlight represents web-marker serialized highlight metadata."""

    id: UUID = Field(primary_key=True)
    textBefore: str
    text: str
    originalText: str
    textAfter: str
    pageId: UUID = Field(foreign_key="page.id")


class AnnotationBase(SQLModel):
    """AnnotationBase represents annotation base class."""

    id: UUID = Field(primary_key=True)
    orgNodeId: Optional[UUID]
    highlightId: UUID = Field(foreign_key="highlight.id")
    pageId: UUID = Field(foreign_key="highlight.pageId")


class AnnotationDB(AnnotationBase, table=True):
    """AnnotationBase represents annotation data to be stored in the db."""

    # Rationale :
    # https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/#only-inherit-from-data-models
    pass


class Annotation(AnnotationBase):
    """Annotation represents annotation data to be used in the API."""

    text: str


class Page(SQLModel, table=True):
    """Page represents a webpage.

    NOTE ???? Page's url should be its primary key because in that way
    the client can be stateless and will not have to store the ids.

    """

    id: UUID = Field(primary_key=True)
    url: AnyUrl
    title: str
