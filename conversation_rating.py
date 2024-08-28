import click

def rate_conversation(cursor, conversation_id):
    """Prompt the user for a binary rating and update the conversation in the database."""
    binary_rating = click.prompt("Please rate this conversation: (0 for Bad, 1 for Good)", type=int)
    cursor.execute("UPDATE user_conversations SET binary_rating = ? WHERE conversation_id = ?", (binary_rating, conversation_id))