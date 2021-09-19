"""This module defines the data models and API schema."""

from sqlmodel import Field, SQLModel
from pydantic import AnyUrl
from uuid import UUID


class Highlight(SQLModel, table=True):
    """Highlight represents web-marker serialized highlight metadata."""

    id: UUID = Field(primary_key=True)
    textBefore: str
    text: str
    originalText: str
    textAfter: str
    pageUrl: AnyUrl = Field(foreign_key="page.url")


class AnnotationBase(SQLModel):
    """AnnotationBase represents annotation base class."""

    id: UUID = Field(primary_key=True)
    orgId: UUID
    highlightId: UUID = Field(foreign_key="highlight.id")
    pageUrl: AnyUrl = Field(foreign_key="highlight.pageUrl")


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

    NOTE Page's url should be its primary key because in that way
    the client can be stateless and will not have to store the ids.

    """

    # id: UUID = Field(primary_key=True)
    url: AnyUrl = Field(primary_key=True)
    title: str
