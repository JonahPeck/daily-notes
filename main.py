import click
from database import get_connection, initialize_database
from get_user_name import get_username
from llm_choice import choose_llm  # Import the model selection function
from dotenv import load_dotenv


@click.command()
def main():
    load_dotenv()  # Load environment variables
    conn = get_connection()  # Get a connection to the database
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries

    initialize_database(cursor)  # Initialize the database (create tables if needed)
    username = get_username()  # Prompt the user for their username

    # Pass the username and cursor to the LLM choice function
    choose_llm(username, cursor)

    conn.commit()  # Commit any changes to the database
    conn.close()  # Close the database connection


if __name__ == "__main__":
    main()
