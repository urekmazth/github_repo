import typer
from rich import print as rich_print
from dotenv import load_dotenv

from github import get_all_user_repositories

load_dotenv()

app = typer.Typer()

repos_app = typer.Typer()

app.add_typer(repos_app, name="repository")


@repos_app.command(help="List all repositories for a given user", name="list")
def list_repositories(username: str = typer.Option(..., "--username", "-u",
                                                   help="Github username")):
    repositories = get_all_user_repositories(username)

    # print repositories in clean json format using rich
    rich_print(repositories)


if __name__ == "__main__":
    app()
