"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Ologist CLI."""


if __name__ == "__main__":
    main(prog_name="ologist-cli")  # pragma: no cover
