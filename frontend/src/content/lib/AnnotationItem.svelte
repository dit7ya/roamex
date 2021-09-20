<script lang="ts">
    import Edit24 from "carbon-icons-svelte/lib/Edit24";
    import Delete24 from "carbon-icons-svelte/lib/Delete24";
    let showItem = true;
    export let highlight;
    export let annotation;
    export let handleEdit;
    export let handleDelete;
</script>

{#if showItem}
    <div class="border border-solid rounded shadow-lg">
        <div class="p-1 mx-1">
            <div class="bg-blue-100 border rounded p-1 m-1">
                {highlight}
            </div>
        </div>
        <p class="p-2 m-1 mx-2">
            {annotation.text}
        </p>
        <div class="flex justify-between">
            <button
                on:click={handleEdit}
                class="px-4 py-2 bg-blue-600 rounded-md text-white outline-none focus:ring-4 hover:bg-blue-800 shadow-lg mx-5 flex font-bold"
            >
                <Edit24 />
            </button>

            <button
                on:click={() => {
                    showItem = false;
                    handleDelete();
                }}
                class="px-4 py-2 bg-blue-600 rounded-md text-white outline-none focus:ring-4 hover:bg-blue-800 shadow-lg mx-5 flex font-bold"
            >
                <Delete24 />
            </button>
        </div>
    </div>
{/if}
