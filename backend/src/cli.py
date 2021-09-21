"""This is the entrypoint of the roamex CLI."""

import typer
import uvicorn


app = typer.Typer()


@app.command()
def hello():
    """Just return a friendly hello."""
    typer.echo("Hello from roamex-cli")


@app.command()
def serve(port: int = 8000):
    """
    Serve the roamex API on the given port.

    Port defaults to 13579.
    """
    typer.echo(f"Serving roamex-api at port {port}...")
    # uvicorn.run("backend.main:app", host="127.0.0.1", port=port, log_level="info")
    uvicorn.run("src.api:app", host="127.0.0.1", port=port, log_level="info")


if __name__ == "__main__":
    app()
