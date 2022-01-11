# Rasa Chatbot and Database

# Rasa Form Store to Database (POSTGRESQL and CSV)
Note: I used psycopg2 (postgresql)
Full Code find in `bot/actions/actions.py`

# Rasa Save Chatbot History (and Custom Columns)
the main coding file on rasa library that save the chat history: `tracker_store.py` 

you can find that file in path (I am using Anaconda IDE) -> `<your_local_path>\anaconda3\envs\<your_environment_name>\Lib\site-packages\rasa\tracker_store.py`

in my directory it goes to `C:\Users\user\anaconda3\envs\rasa_env\Lib\site-packages\rasa\tracker_store.py`

To find the custom part of the `tracker_store.py` that i have made before to add column `bot_id` and `channel_source` to database. you can check on `custom_postgre_tracker_store.py` and find a comment with text -> `# CUSTOM_TRACKER`
