import click
from open_ai_conversation import open_ai_llm


def choose_llm(username, cursor):
    model = click.prompt(
        "Choose the LLM you would like to use",
        type=click.Choice(["chat gpt", "llama", "replicate"]),
    )
    click.echo(f"You chose {model}")
    if model.lower() == "chat gpt":
        open_ai_llm(username, cursor)
    elif model.lower() == "llama":
        click.echo("Model not yet supported")
    elif model.lower() == "replicate":
        click.echo("Model not yet supported")
