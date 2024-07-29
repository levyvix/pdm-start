from typer import Typer
import typer

app = Typer()


@app.command()
def hello(name: str):

    print("hello", name)


@app.command()
def bye(name: str):

    print("bye bye", name)


if __name__ == "__main__":
    app()
