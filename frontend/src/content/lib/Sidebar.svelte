<script>
  import hotkeys from "hotkeys-js";
  import { fly } from "svelte/transition";
  import AnnotationsList from "./AnnotationsList.svelte";

  let showSidebar = false;
  const toggleSidebar = () => {
    showSidebar = !showSidebar;
  };

  hotkeys("ctrl+alt+s", () => {
    toggleSidebar();
  });
</script>

{#if showSidebar}
  <div id="roamex-sidebar" transition:fly={{ x: 200, duration: 100 }}>
    <div
      class="rounded border border-solid border-opacity-80 shadow-2xl shadow-gray-900 bg-gray-100 p-4 m-4 min-h-full shadow-lg"
    >
      <AnnotationsList />
    </div>
  </div>
{/if}

<style>
  #roamex-sidebar {
    all: unset;
    font-size: 14px;
    /* font-family: sans-serif; */
    /* color: black; */
    position: fixed;
    top: 0;
    height: 90vh;
    right: 0;
    width: 40vw;
    z-index: 999999999;
    overflow-y: auto;
  }
</style>
