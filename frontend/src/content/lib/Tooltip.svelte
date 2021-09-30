<script>
  import { AlignLeftIcon, Edit3Icon } from "svelte-feather-icons";
  export let left;
  export let top;
  export let handleHighlightClick;
  export let handleAnnotateClick;
</script>

<div id="roamex-tooltip" style="--posleft: {left}; --postop: {top};">
  <div class="flex">
    <button
      on:click={handleHighlightClick}
      class="px-2 py-1 bg-blue-500 rounded-md text-white outline-none focus:ring-4 hover:bg-blue-800 shadow-lg flex font-bold m-1"
    >
      <Edit3Icon size="15" />
    </button>

    <button
      on:click={handleAnnotateClick}
      class="px-2 py-1 bg-blue-500 rounded-md text-white outline-none focus:ring-4 hover:bg-blue-800 shadow-lg flex font-bold m-1"
    >
      <AlignLeftIcon size="15" />
    </button>
  </div>
</div>

<style>
  #roamex-tooltip {
    position: absolute;
    left: var(--posleft);
    top: var(--postop);
    z-index: 9999999;
  }
</style>
