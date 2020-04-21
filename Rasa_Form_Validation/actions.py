# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

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

# class ActionHelloWorld(FormAction):
# 
#      def name(self) -> Text:
#          return "admission_form"
#      
# 
#      @staticmethod
#      def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         
#         print("required_slots(tracker: Tracker)")
#         return ["name",  "ssn", "subject"]
# 
#      def submit(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any],
#      ) -> List[Dict]:
# 
#          dispatcher.utter_message(template="utter_submit")
# 
#          return []

class ActionHelloWorld(FormAction):

     def name(self) -> Text:
         return "admission_form"
     

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        
        print("required_slots(tracker: Tracker)")
        return ["name",  "ssn", "subject_code"]

     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        print("slot_mappings(self) ")

        return {
            
            "subject_code": [
                self.from_entity(entity="subject", intent="subject_entry"),
                
            ],
            
     }
     
     @staticmethod
     def subject_db() -> List[Text]:
        """Database of supported cuisines"""
     
        #print("subject_db() ")
        return [
            "physics",
            "computer",
            "zoologu",
            "biology",
            "chemistry",
            
        ]

     def validate_subject_code(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
     ) -> Dict[Text, Any]:
        """Validate subject_code value."""

        print("ivalidate_subject_code() method  ", value)
        if value.lower() in self.subject_db():
            # validation succeeded, set the value of the "subject_code" slot to value
            return {"subject_code": value}
        else:
            dispatcher.utter_message(template="utter_wrong_subject")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"subject_code": None}

     def validate_ssn(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
     ) -> Dict[Text, Any]:
        """Validate ssn value."""

        print("ivalidate_ssn() method  ", value)
        if len(value) == 6:
            # validation succeeded, set the value of the "ssn" slot to value
            return {"ssn": value}
        else:
            dispatcher.utter_message(template="utter_wrong_ssn")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"ssn": None}       

     def submit(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any],
     ) -> List[Dict]:

         dispatcher.utter_message(template="utter_submit")

         return []
