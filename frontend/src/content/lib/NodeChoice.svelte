<script>
    import { onMount } from "svelte";
    // Importing Autocomplete like this cause this bug https://github.com/rob-balfre/svelte-select/issues/128#issuecomment-632391193
    import AutoComplete from "simple-svelte-autocomplete/src/SimpleAutocomplete.svelte";
  // import {
  //     getHeadlines,
  //     getOrgRoamFiles,
  // } from "../apiCalls.js";

    let nodes;
    let orgFiles;
    onMount(async () => {
        orgFiles = await getOrgRoamFiles();
    });

    export let selectedFile;
    export let selectedNode;
    // $: console.log(selectedNode);
    const handleFileSelect = async () => {
        // Get the nodes for the current file

        if (selectedFile) {
            nodes = (await getHeadlines(selectedFile.file)).map(
                (node, idx) => ({ idx, title: node })
            );
        }
    };
</script>

<div class="flex justify-between w-full">
    <div class="border rounded max-w-1/2">
        <AutoComplete
            items={orgFiles}
            bind:selectedItem={selectedFile}
            onChange={handleFileSelect}
            showClear
            hideArrow
            labelFieldName="title"
            placeholder="Choose file..."
        />
    </div>

    <div class="border rounded max-w-1/2">
        <AutoComplete
            items={nodes}
            bind:selectedItem={selectedNode}
            showClear
            hideArrow
            labelFieldName="title"
            placeholder="Choose heading..."
        />
    </div>
</div>

<style>
 :global(.autocomplete) {
     all: unset;
 }
</style>
