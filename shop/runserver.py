import typer
from shop.asgi import application

cli = typer.Typer()


@cli.command()
def runserver(host: str = "localhost", port: int = 8000, debug: bool = True):
    try:
        import uvicorn
    except ImportError:
        typer.echo("Cannot star server, install uvicorn at first", err=True)
        raise typer.Exit(code=1)

    typer.echo("Starting server ...")
    uvicorn.run(application, host=host, port=port, debug=debug)


if __name__ == "__main__":
    cli()
