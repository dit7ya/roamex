const fs = require("fs");
const esbuild = require("esbuild");
const sveltePlugin = require("esbuild-svelte");
// import autoPreprocess from 'svelte-preprocess';
const autoPreprocess = require("svelte-preprocess");
// import { windi } from "svelte-windicss-preprocess";
const { windi } = require("svelte-windicss-preprocess");

// make sure the directoy exists before stuff gets put into it
if (!fs.existsSync("./dist/")) {
  fs.mkdirSync("./dist/");
}

// build the application
esbuild
  .build({
    entryPoints: ["./src/content/index.js"],
    outdir: "./dist",
    format: "iife",
    minify: false, // so the resulting code is easier to understand
    bundle: true,
    splitting: false,
    incremental: false,
    plugins: [
      sveltePlugin({
        compileOptions: { css: true },
        preprocess: [windi({}), autoPreprocess()],
      }),
    ],
    watch: {
      onRebuild(error, result) {
        if (error) console.error("watch build failed:", error);
        else console.log("watch build succeeded:", result);
      },
    },
  })
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
