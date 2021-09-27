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
    pageId: UUID = Field(foreign_key="pagedb.id")


class AnnotationBase(SQLModel):
    """AnnotationBase represents annotation base class."""

    id: UUID = Field(primary_key=True)
    orgNodeId: Optional[UUID]
    highlightId: UUID = Field(foreign_key="highlight.id")
    pageId: UUID = Field(foreign_key="highlight.pageId")


class AnnotationDB(AnnotationBase, table=True):
    """AnnotationDB represents annotation data to be stored in the db."""

    # Rationale :
    # https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/#only-inherit-from-data-models
    pass


class Annotation(AnnotationBase):
    """Annotation represents annotation data to be used in the API."""

    text: str


class PageBase(SQLModel):
    """PageBase is the core of the page model."""

    id: UUID = Field(primary_key=True)
    url: AnyUrl
    title: str


class PageDB(PageBase, table=True):
    """The page schema for the DB."""

    pass


class Page(PageBase):
    """Page represents a webpage in the API."""

    pageComment: Optional[str]


class PageComment(SQLModel):
    text: str
