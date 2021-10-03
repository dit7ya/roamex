from .models import Highlight, Page, Annotation
from functools import lru_cache

# from orgparse import load
from src import dbops

from uuid import UUID
from pathlib import Path

import yaml

import os

# Get config


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


def replace_in_file(old_content, new_content, filepath):
    """Replace the old_content with the new_content."""
    with open(filepath, "r") as f:
        filedata = f.read()
        filedata = filedata.replace(old_content, new_content)
    with open(filepath, "w") as f:
        f.write(filedata)


def append_in_file(headline_and_body, new_subtree, filepath):
    """Append the new_subtree to the headline_and_body.

    Usage of this currently works for the toplevel content only,
    and not the children nodes.
    """
    new_headline_and_body = headline_and_body + "\n" + new_subtree

    with open(filepath, "r") as f:
        filedata = f.read()
        filedata = filedata.replace(headline_and_body, new_headline_and_body)
    with open(filepath, "w") as f:
        f.write(filedata)


config = get_config()

org_roam_directory = config["org_roam_directory"]


def create_roamex_directory():
    """Create roamex directory inside org_roam_directory if does not already exist."""
    roamex_dir_location = f"{org_roam_directory}/roamex/"
    if not os.path.exists(roamex_dir_location):
        os.makedirs(roamex_dir_location)

    return


###########################################################
# Page
###########################################################


def create_page(page: Page):
    """Create new page under Roamex directory."""
    # Path.mkdir(org_roam_directory, exist_ok=True)  # FIXME better

    filename = str(page.id) + ".org"

    file_content = (
        ":PROPERTIES:\n"
        f":ID:       {page.id}\n"
        f":ROAM_REFS: {page.url}\n"
        ":END:\n"
        f"#+title: {page.title}\n"
        "\n"
        f"{page.pageComment if page.pageComment else ''}\n\n"  # REVIEW Does this work?
        f"* Highlights\n"
        f"* Annotations\n"
    )

    # Create a new file, based on page attributes
    with open(org_roam_directory + "/roamex/" + filename, "w") as orgFile:
        # TODO Raise Error if file already exists
        orgFile.write(file_content)


# TODO read_page_comment


def update_page_comment(pageId: UUID, pageComment: str):

    pageLocation = f"{org_roam_directory}/roamex/{pageId}.org"

    # HACK orgparse thinks root node cannot have PROPERTIES
    # and returns the body from  orgFile.root.body without newlines
    # so let us just do it in pure python
    #
    # REVIEW what if user enters more properties?? TODO
    # TODO This is again ugly hack cause update will append instead
    # of replacing

    # HACK prepend `* Highlights` with pageComment
    old_content = "* Highlights"
    new_content = pageComment + "\n\n* Highlights"
    # print(new_content)

    replace_in_file(old_content, new_content, pageLocation)


## Read
## Update - NOTE not required
## Delete - NOTE not required

###########################################################
#### Highlights
###########################################################


## Create


def create_highlight(highlight: Highlight):
    # Highlights are always stored in the dedicated roamex page file

    pageLocation = f"{org_roam_directory}/roamex/{highlight.pageId}.org"

    content = (
        f"** {highlight.originalText}\n"
        f":PROPERTIES:\n"
        f":ID: {highlight.id}\n"
        f":ROAM_EXCLUDE: t\n"
        f":END:\n"
    )

    # HACK append before the annotation node

    old_content = "* Annotations"
    new_content = content + "\n\n* Annotations"

    replace_in_file(old_content, new_content, pageLocation)


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
        pageLocation = f"{org_roam_directory}/roamex/{annotation.pageId}.org"

        highlightId = annotation.highlightId
        highlight_text = dbops.read_highlight(highlightId).originalText

        content = (
            f"** Annotation on [[id:{highlightId}][{highlight_text}]]\n"
            ":PROPERTIES:\n"
            f":ID: {annotation.id}\n"
            f":ROAM_EXCLUDE: t\n"
            ":END:\n"
            "\n"
            f"{annotation.text}\n"
        )

        # HACK Just append to the file
        with open(pageLocation, "a") as f:
            f.write(content)

        return
    # TODO the other case


# Read
## Update
## Delete
