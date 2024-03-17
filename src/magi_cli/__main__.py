"""Command-line interface."""

import click
from cookiecutter.main import cookiecutter


@click.group()
@click.version_option()
def main() -> None:
    """Magi."""


@main.command()
def new() -> None:
    """Generate a new Magi project."""
    cookiecutter(
        # Replace with "get_repository_for_template" method that parses the
        # .magi.yml and works out which repository a given template is stored in.
        "git@github.com:ologistio/base.git",
        # Replace with the template name
        directory="new",
        # Replace with "lockfile.new_version_available" to determine if the file
        # has changed on the remote and meets the version requirements in .magi.yml
        overwrite_if_exists=True,
        # Capture input with something nicer than Cookiecutter? Or just keep
        # it simple?
        no_input=True,
    )
