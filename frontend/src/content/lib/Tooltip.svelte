<script>
  export let left;
  export let top;
  export let handleClick;
</script>

<div id="roamex-tooltip" style="--posleft: {left}; --postop: {top};">
  <button
    on:click={handleClick}
    class="px-4 py-2 bg-blue-600 rounded-md text-white outline-none focus:ring-4 hover:bg-blue-800 shadow-lg mx-5 flex font-bold"
  >
    Highlight!
  </button>
</div>

<style>
  #roamex-tooltip {
    position: absolute;
    left: var(--posleft);
    top: var(--postop);
    z-index: 9999999;
  }
</style>
