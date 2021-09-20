<script>
  // import Marker from "./lib/Marker.svelte";
  import Sidebar from "./lib/Sidebar.svelte";
  import Main from "./lib/Main.svelte";
</script>

<div class="roamex-global">
  <div class="font-sans text-gray-900">
    <!-- <Marker /> -->
    <Main />
    <Sidebar />
  </div>
</div>

<style windi:preflights:global windi:safelist:global>
  .roamex-global {
    all: unset;
  }

  :global(.roamex-hide-me) {
    display: none;
  }

  :global(.roamex-link) {
    color: blueviolet;
    text-decoration-style: solid;
    text-decoration-line: underline;
  }
</style>
