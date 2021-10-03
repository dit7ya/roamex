<script lang="ts">
    import { v4 as uuidv4 } from "uuid";
    import { createMarker } from "../marker";
    import Tooltip from "./Tooltip.svelte";
    import { Page, Highlight, Annotation } from "../apiCalls";
    import type { PageType, HighlightType, AnnotationType } from "../models";
    import { onMount } from "svelte";
    import NextEditor from "./NextEditor.svelte";

    import hotkeys from "hotkeys-js";

    let showTooltip = false;
    let showAnnotationEditor = false;
    let posLeft;
    let posTop;
    let highlight: HighlightType;
    let serialized;
    let annotation: AnnotationType;
    let annotationText;

    let showPageCommentEditor = false;
    let pageComment;

    let pageId;

    const marker = createMarker();
    onMount(() => {
        // Do we have this page in our db?

        const url = document.location.href;

        Page.readPage(url).then((page) => {
            console.log(page);
            if (page.message == "Page does not exist") {
                return null;
            } else {
                pageId = page.id;
                Highlight.getHighlights(pageId).then((highlights) => {
                    highlights.map((x) => {
                        console.log(x);
                        const { pageId, ...h } = x;
                        h.uid = h.id; // TODO FIXME HACK
                        marker.paint(h);
                    });
                });
            }
        });

        hotkeys("shift+c", () => {
            handlePageCommentShow()
        });
    });

    const createOrGetPageId = () => {
        // If page exists in db, get its id, else create a new id and return it
        // TODO implement this
        return;
    };

    const handlePageCommentShow = () => {
        showPageCommentEditor = true;
    };

    const handlePageCommentSubmit = () => {
        showPageCommentEditor = false;

        // do we have this page in the db?
        if (pageId) {
            Page.createOrUpdatePageComment(pageId, pageComment);
        } else {
            // create a new page along with the comment

            pageId = uuidv4();

            const url = document.location.href;
            const title = document.title;
            // console.log(pageId);
            const thisPage: PageType = {
                id: pageId,
                url: url,
                title: title,
                pageComment: pageComment,
            };

            console.log(thisPage);
            Page.createPage(thisPage).then(() =>
                console.log("Page created along with comment.")
            );
        }
    };

    // const handleMouseup = async () => {
    const handleMouseup = () => {
        const selection = window.getSelection();
        console.log("handleMouseUp being executed, selection is", selection);

        if (selection.isCollapsed) {
            showTooltip = false;
            return null;
        } else {
            // console.log(selection);
            const range = selection.getRangeAt(0);
            serialized = marker.serializeRange(range);
            // console.log(serialized);

            posLeft = range.getBoundingClientRect().x + window.scrollX + "px";
            posTop =
                range.getBoundingClientRect().y +
                range.getBoundingClientRect().height +
                window.scrollY +
                10 +
                "px"; // IT is insane that this computation is doable in js

            showTooltip = true;
            console.log("showTooltip is becoming", showTooltip);
        }
    };

    // TODO
    ///const createPageIfNotexist = () => {
    //
    //}

    const handleHighlightClick = () => {
        showTooltip = false;

        const url = document.location.href;
        const title = document.title;

        console.log(pageId);
        // Do we already have this page created?
        if (!pageId) {
            // Create page
            pageId = uuidv4();
            // console.log(pageId);
            const thisPage: PageType = {
                id: pageId,
                url: url,
                title: title,
            };
            Page.createPage(thisPage).then(() => console.log("Page created"));
        }
        highlight = {
            id: serialized.uid, // TODO IMPORTANT REVIEW HOW UID becomes id
            textBefore: serialized.textBefore,
            text: serialized.text,
            originalText: serialized.originalText,
            textAfter: serialized.textAfter,
            pageId: pageId,
        };
        console.log(highlight);

        marker.paint(serialized);
        Highlight.createHighlight(highlight);
    };

    const handleAnnotationClick = () => {
        handleHighlightClick(); // REVIEW if this will provide highlight and page id

        showAnnotationEditor = true;
    };

    const handleAnnotationSubmit = () => {
        showAnnotationEditor = false;

        const annotationId = uuidv4();
        annotation = {
            id: annotationId,
            // orgNodeId: '', // FIXME REVIEW
            highlightId: serialized.uid,
            pageId: pageId,
            text: annotationText,
        };

        Annotation.createAnnotation(annotation);
    };

    // const callPageComment = () => {
    // createPageIfNotexist()
    // TODO capture comment text
    // TODO send the text to the page
    //}
</script>

<svelte:window on:mouseup={handleMouseup} />


<div>
    {#if showTooltip}
        <div>
            <Tooltip
                left={posLeft}
                top={posTop}
                {handleHighlightClick}
                handleAnnotateClick={handleAnnotationClick}
            />
        </div>
    {/if}
    {#if showAnnotationEditor}
        <!-- TODO need to discard the selected highlight a-->
        <NextEditor
            bind:editorContent={annotationText}
            handleClick={() => handleAnnotationSubmit()}
            handleClose={() => {
                showAnnotationEditor = false;
            }}
        />
    {/if}

    {#if showPageCommentEditor}
        <NextEditor
            bind:editorContent={pageComment}
            handleClick={() => handlePageCommentSubmit()}
            handleClose={() => {
                showPageCommentEditor = false;
            }}
        />
    {/if}
</div>
