<script>
    import Tribute from "tributejs";
    import { onMount } from "svelte";
  import { getOrgRoamNodes } from "../apiCalls.js";
  // import NodeChoice from "./NodeChoice.svelte";

    export let editorContent = "";
    export let handleClick;
  // export let selectedFile;
  // export let selectedNode;

    onMount(async () => {
        const orgNodes = await getOrgRoamNodes();
        console.log(orgNodes)

        let values = orgNodes.map((x) => ({ key: x.title, value: x.id }));

        const tribute = new Tribute({
            autocompleteMode: true,
            noMatchTemplate: "",
            values,
            selectTemplate(item) {
                if (typeof item === "undefined") {
                    return null;
                }

                if (this.range.isContentEditable(this.current.element)) {
                    // TODO reformat this with template strings
                    return (
                        '<span class="roamex-link" contenteditable="false"><a>' +
                        `<p class= "roamex-hide-me">[[id:${item.original.value}][</p>` +
                        item.original.key +
                        '<p class="roamex-hide-me">]]</p>' +
                        "</a></span>"
                    );
                }

                return item.original.value;
            },
            menuItemTemplate(item) {
                return `<div class="roamex-menu-item">${item.string}</div>`;
            },
            menuShowMinLength: 2,
            menuItemLimit: 7,
            // menuContainer: document.getElementById("roamex-app").shadowRoot
        });
        // tribute.attach(document.querySelectorAll(".mentionable"));
        tribute.attach(document.getElementById("roamex-app").shadowRoot.querySelector(".mentionable"));
    });
</script>

<div
    class="roamex-next-editor p-4 m-2 bg-gray-50 border border-solid border-teal rounded "
>
    <!-- <div id="roamex-menu" /> -->
    <div>
        <div
            contenteditable="true"
            class="mentionable min-w-full min-h-32 border rounded bg-teal-50 border-solid"
            bind:textContent={editorContent}
        />

        <!-- <div class="flex my-4">
             <NodeChoice bind:selectedFile bind:selectedNode />
             </div> -->
        <button
            on:click={() => {
                handleClick();
                editorContent = "";
            }}
            class="px-4 py-2 bg-blue-600 rounded-md text-white outline-none focus:ring-4 hover:bg-blue-800 shadow-lg mx-5 flex font-bold"
        >
            Save</button
        >
    </div>
</div>

<style>
    .roamex-next-editor {
        position: fixed;
        top: 10%;
        left: 0%;
        width: 40%;
        z-index: 999;
    }
</style>
