<script lang="ts">
    import { v4 as uuidv4 } from "uuid";
    import { createMarker } from "../marker";
    import Tooltip from "./Tooltip.svelte";
    import { Page, Highlight } from "../apiCalls";
    import type { PageType, HighlightType } from "../models";
    import { onMount } from "svelte";
    import AnnotationsList from "./AnnotationsList.svelte";

    let showTooltip = false;
    let posLeft;
    let posTop;
    let highlight: HighlightType;
    let serialized;

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
    });

    // const handleMouseup = async () => {
    const handleMouseup = () => {
        const selection = window.getSelection();
        console.log("handleMouseUp being executed, selection is", selection);

        if (selection.isCollapsed) {
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

            const url = document.location.href;
            const title = document.title;

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
                Page.createPage(thisPage).then(() =>
                    console.log("page created")
                );
            } else {
                highlight = {
                    id: serialized.uid, // TODO IMPORTANT REVIEW HOW UID becomes id
                    textBefore: serialized.textBefore,
                    text: serialized.text,
                    originalText: serialized.originalText,
                    textAfter: serialized.textAfter,
                    pageId: pageId,
                };
                // console.log(highlight);

                showTooltip = true;
                console.log("showTooltip is becoming", showTooltip);
            }
        }
    };

    const handleHighlightClick = () => {
        showTooltip = false;
        marker.paint(serialized);
        Highlight.createHighlight(highlight);
    };
</script>

<svelte:window on:mouseup={handleMouseup} />

<div>
    {#if showTooltip}
        <div>
            <Tooltip
                left={posLeft}
                top={posTop}
                handleClick={handleHighlightClick}
            />
        </div>
    {/if}
</div>
