from database import engine
from sqlmodel import Session
from .models import Highlight, AnnotationBase, Page, Annotation
from functools import lru_cache
from orgparse import load
from src import dbops

from pathlib import Path

# from yaml import FullLoader
import yaml

## Get config


@lru_cache()
def get_config() -> dict:
    """Load the config from ~/.config/roamex/config.yaml.

    Returns:
        A dict with the config variables.
    """
    # Load config file
    # Due to the nature of ASGI applications, it is not usual to
    # run them programmatically
    # See more at something like https://github.com/mamba-org/quetz/pull/29
    user_home = str(Path.home())
    with open(f"{user_home}/.config/roamex/config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    return config


def replace_in_file(headline_and_body, new_subtree, filepath):
    """Append the new_subtree to the headline_and_body."""
    new_headline_and_body = headline_and_body + "\n" + new_subtree

    with open(filepath, "r") as f:
        filedata = f.read()
        filedata = filedata.replace(headline_and_body, new_headline_and_body)
    with open(filepath, "w") as f:
        f.write(filedata)


config = get_config()

org_roam_directory = config["org_roam_directory"]


###########################################################
# Page
###########################################################


def create_page(page: Page):
    """Create new page under Roamex directory."""
    Path.mkdir(org_roam_directory, exist_ok=True)  # FIXME better

    filename = page.id + ".org"

    file_content = (
        ":PROPERTIES:"
        f":ID:       {page.id}"
        f":ROAM_REFS: {page.url}"
        ":END:"
        f"#+title: {page.title}"
        ""
        f"* Highlights"
        f"* Annotations"
    )

    # Create a new file, based on page attributes
    with open(org_roam_directory + filename, "w") as orgFile:
        # TODO Raise Error if file already exists
        orgFile.write(file_content)


## Read
## Update - NOTE not required
## Delete - NOTE not required

###########################################################
#### Highlights
###########################################################


## Create


def create_highlight(highlight: Highlight):
    # Highlights are always stored in the dedicated roamex page file

    pageLocation = f'{org_roam_directory} + "/roamex/" + {highlight.pageId} + .org'

    orgFile = load(pageLocation)

    content = (
        f"** {highlight.originalText}\n"
        f":PROPERTIES:\n"
        f":ID: {highlight.id}\n"
        f":END:\n"
    )
    # Highlights is the 1st node REVIEW
    highlight_node = str(orgFile[1])
    replace_in_file(highlight_node, content, pageLocation)


## Read - NOTE not required
## Update - NOTE not required

## Delete
# def delete_highlight(id):


###########################################################
#### AnnotationBase
###########################################################

## Create
def create_annotation(annotation: Annotation):

    # If orgNodeId is not provided, create annotation on the orgFile
    if not annotation.orgNodeId:
        # TODO
        pageLocation = f'{org_roam_directory} + "/roamex/" + {annotation.pageId} + .org'

        highlightId = annotation.highlightId
        highlight_text = dbops.read_highlight(highlightId)["originalText"]

        orgFile = load(pageLocation)

        content = (
            f"** Annotation on [[id:{highlightId}][{highlight_text}]]\n"
            ":PROPERTIES:\n"
            f":ID: {annotation.id}\n"
            ":END:\n"
            "\n"
            f"{annotation.text}\n"
        )
        # Annotation is the 2nd node REVIEW
        annotation_node = str(orgFile[2])
        replace_in_file(annotation_node, content, pageLocation)

        return
    # TODO the other case


## Read
## Update
## Delete
