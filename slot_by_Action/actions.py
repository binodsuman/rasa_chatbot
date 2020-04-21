# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         name = tracker.get_slot("name")
         country = tracker.get_slot("country")

         leader_name = ""
         if country.lower() == "us":
             leader_name = "Donald Trump"
         elif country.lower() == "india":
             leader_name = "Mr. Modi"
         else:
             leader_name = "Data base is not avaible"

         message = " {} belongs to {} and leader name is {}".format(name,country, leader_name)
         #message = name +" belongs to "+ country +" and your country leader is "+leader_name
         print(message)
         dispatcher.utter_message(text=message)

         return [SlotSet("leader", leader_name)]
         #return []
