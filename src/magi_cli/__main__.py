"""Command-line interface."""

from typing import List

import click
from cookiecutter.main import cookiecutter


DEFAULT_REPOSITORIES = ["git@github.com:ologistio/base.git"]


@click.group()
@click.version_option()
def main() -> None:
    """Magi."""


@main.command()
@click.argument("name")
@click.option(
    "-d",
    "--dry-run",
    is_flag=True,
    show_default=True,
    default=False,
    help="Reports changes that would be made, but does not change the filesystem.",
)
@click.option(
    "-g",
    "--skip-git",
    is_flag=True,
    show_default=True,
    default=False,
    help="Skip git repository initialisation.",
)
@click.option(
    "-i",
    "--skip-install",
    is_flag=True,
    show_default=True,
    default=False,
    help="Skip package/repository installation.",
)
@click.option(
    "-f",
    "--force",
    is_flag=True,
    show_default=True,
    default=False,
    help="Force creation in current directory.",
)
@click.option(
    "-r",
    "--repository",
    multiple=True,
    default=None,
    help="Specify schematics repository. Repeatable.",
)
def new(
    name: str,
    dry_run: bool,
    skip_git: bool,
    skip_install: bool,
    false: bool,
    repository: List[str] = DEFAULT_REPOSITORIES,
) -> None:
    """Creates and initializes a new Magi project.

    Creates a folder with the given <name> and populates the folder with
    configuration files; then creates sub-folders for foo (/foo), bar (/bar)
    and baz (/baz) and populates them with default files for infra components
    and tests.
    """
    cookiecutter(
        # Replace with "get_repository_for_template" method that parses the
        # .magi.yml and works out which repository a given template is stored in.
        DEFAULT_REPOSITORIES[0],
        # Replace with the template name
        directory="new",
        # Replace with "lockfile.new_version_available" to determine if the file
        # has changed on the remote and meets the version requirements in .magi.yml
        overwrite_if_exists=True,
        # Capture input with something nicer than Cookiecutter? Or just keep
        # it simple?
        no_input=True,
    )
