from os import sep
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from uuid import uuid4
import pandas as pd
import psycopg2

# CSV Database
admindb_path = 'C:/Users/user/Anaconda Project/Widya x BK/WIN Research/database/data/db_csv/admin_db.csv'

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_register_admin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Generate Password
        userid = str(uuid4())
        username = tracker.get_slot('ENT_USERNAME')
        password = uuid4().hex
        
        userdb = pd.read_csv(admindb_path, sep='\t')
        
        # Check if username existing in admin_db.csv 
        # If use SQL, fetch all username from database and change to list or something else
        if username not in userdb['username'].tolist(): # This Condition based on CSV Database
            # Send Account Summary
            dispatcher.utter_message(text="Your account details:  \nUsername : {}  \nPassword: {}  \nI am glad to help you!".format(username, password))
            
            # Save Data to CSV using Pandas -----------------------------------------------------------------------------------------
            userdb.loc[-1] = [userid, username, password]
            userdb.to_csv(admindb_path, index=False, sep='\t')

            # Save Data to PostgreSQL -----------------------------------------------------------------------------------------------
            conn = psycopg2.connect(database = "chatbot_db", user = "postgres", password = "admin", host = "127.0.0.1", port = "5432")
            cur = conn.cursor()

            cur.execute("INSERT INTO accounts (userid, username, password) VALUES (%s, %s, %s)", (userid, username, password))

            conn.commit()
            conn.close()
        else:
            dispatcher.utter_message(text="Username have been used!")
            
        return []
