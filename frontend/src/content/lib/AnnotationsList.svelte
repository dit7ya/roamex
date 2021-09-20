<script lang="ts">
    import AnnotationItem from "./AnnotationItem.svelte";
  // import { getHighlights } from "./../apiCalls";
  // import { cudNote } from "./../apiCalls";

    const url = document.location.href;
    let promise = getHighlights(url);

</script>

<div>
    {#await promise}
        <p>... loading</p>
    {:then notes}
        {#each notes as note}
            <div class="m-3">
                <AnnotationItem
                    highlight={note.highlight.originalText}
                    annotation={note.annotation}
                    handleEdit={() => console.log("Edit has been clicked.")}
                    handleDelete={() => {
                        cudNote("delete", note);
                    }}
                />
            </div>
        {/each}
    {/await}
</div>
