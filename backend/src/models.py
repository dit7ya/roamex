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
    pageId: UUID = Field(foreign_key="page.id")


class AnnotationBase(SQLModel, table=True):
    """AnnotationBase represents annotation data to be stored in the db."""

    id: UUID = Field(primary_key=True)
    orgId: UUID
    highlightId: UUID = Field(foreign_key="highlight.id")


class Annotation(AnnotationBase):
    """Annotation represents annotation data to be used in the API."""

    text: str


class Page(SQLModel, table=True):
    """Page represents a webpage."""

    id: UUID = Field(primary_key=True)
    url: AnyUrl
    title: str


# class OrgFile(BaseModel):
#     filepath: FilePath
#     node_idx: Optional[int]


# class Note(BaseModel):
#     """
#     Data model for a Note.

#     A Note is a highlight + annotation + page_metadata + file_metadata
#     """

#     highlight: Highlight
#     annotation: Annotation
#     page: Page
#     orgfile: OrgFile
