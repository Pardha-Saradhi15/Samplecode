from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker

from rasa_sdk.executor import CollectingDispatcher

import webbrowser

 

 

 

class Actionvideo(Action):

 

 

 

    def name(self) -> Text:

        return "action_get_url"

 

 

 

    async def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        video_url = "https://youtu.be/7ycmTUK3Uzk"

        dispatcher.utter_message("Wait playing your video.")

        webbrowser.open(video_url)

        return []