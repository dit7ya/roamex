<script lang="ts">
  import {marker} from "../marker"

    import Tooltip from "./Tooltip.svelte";
    import NextEditor from "./NextEditor.svelte";

    let lastRange;
    let posLeft;
    let posTop;
    let lastSerialized;

    let selectedFile;
    let selectedNode;
    $: console.log(selectedFile);
    $: console.log(selectedNode);

    const retrievePageHighlights = async () => {
        const url = document.location.href;
        const highlightsAndAnnotations = await getHighlights(url);

        // Console.log(highlightsAndAnnotations);
        highlightsAndAnnotations.map((x) => {
            console.log(x.highlight);
            marker.paint(x.highlight);
        });

        return highlightsAndAnnotations;
    };

    retrievePageHighlights().then(console.log("Page highlights retrieved."));

    let showTooltipActions = false;
    const showTooltip = (range) => {
        // Given a range object, show a tooltip near the range
        // which contains a button for highlighting
        // when clicked execute a highlight paint on the range

        lastRange = range;
        // Adding window.scrollX and window.scrollY so that we can do absolute positioning
        // FIXME But this will fail if there are nested scrollable elements

        posLeft = range.getBoundingClientRect().x + window.scrollX + "px";
        posTop =
            range.getBoundingClientRect().y +
            range.getBoundingClientRect().height +
            window.scrollY +
            10 +
            "px"; // IT is insane that this computation is doable in js
        showTooltipActions = true;
    };
    const annotate = () => {
        showEditor = false;

        const text = JSON.stringify({
            metadata: lastSerialized,
            annotation: editorContent,
        });

        const url = document.location.href;
        const pageTitle = document.title;

        const note = {
            highlight: {
                uid: lastSerialized.uid,
                textBefore: lastSerialized.textBefore,
                text: lastSerialized.text,
                originalText: lastSerialized.originalText,
                textAfter: lastSerialized.textAfter,
            },
            annotation: { text: editorContent },
            page: {
                url: url,
                title: pageTitle,
            },
            orgfile: {
                filepath: selectedFile.file,
                node_idx: selectedNode.idx,
            },
        };
        cudNote("create", note).then(console.log);


        return text;
    };

    const highlight = (range) => {
        // Given a range, paint the range with highlight
        // show a comment box for inputting comment
        // and return the serialized object along with
        // the comment

        lastSerialized = marker.serializeRange(range);
        // console.log("hello", lastSerialized);
        marker.paint(lastSerialized);
        // Console.log(serialized);

        showTooltipActions = false;
        showEditor = true;
    };

    marker.addEventListeners();
    const handleMouseup = () => {
        const selection = window.getSelection();
        // Console.log(selection)
        if (selection.isCollapsed) {
            return null;
        }

        const range = selection.getRangeAt(0);
        // Console.log(range)

        showTooltip(range);
    };

    let showEditor = false;
    let editorContent = "";
</script>

<svelte:window on:mouseup={handleMouseup} />

<div>
    {#if showEditor}
        <div class="bg-red-100">
            <NextEditor
                handleClick={() => console.log(annotate())}
                bind:selectedFile
                bind:selectedNode
                bind:editorContent
            />
        </div>
    {/if}
    {#if showTooltipActions}
        <div class="">
            <Tooltip
                left={posLeft}
                top={posTop}
                handleClick={() => highlight(lastRange)}
            />
        </div>
    {/if}
</div>
