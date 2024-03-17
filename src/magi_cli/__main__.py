"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Magi."""


if __name__ == "__main__":
    main(prog_name="magi")  # pragma: no cover
