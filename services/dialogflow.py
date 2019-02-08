import os
import dialogflow_v2 as df
import logging
from services.actionHandler import actionHandler
from google.protobuf.json_format import MessageToJson

class dialogflow:
    
    def __init__(self):
        self.project_id = os.getenv('DIALOG_FLOW_PROJECT_ID')
        self.language_code = 'en-US'

    # detect_intent_texts('1',['How old are you?'])
    def detect_intent_texts(self, session_id, texts):
        """Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversaion."""
        session_client = df.SessionsClient()

        session = session_client.session_path(self.project_id, session_id)
        logging.debug('Session path: {}\n'.format(session))
        res = {}
        res["say"] = []
        for text in texts:
            # pylint: disable=E1101
            text_input = df.types.TextInput(
                text=text, language_code=self.language_code)

            query_input = df.types.QueryInput(text=text_input)

            response = session_client.detect_intent(
                session=session, query_input=query_input)

            logging.debug('Query text: {}'.format(response.query_result.query_text.encode('utf-8')))
            logging.debug('Detected intent: {} (confidence: {})\n'.format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence))
            logging.debug('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
            res["say"].append(response.query_result.fulfillment_text)
            if response.query_result.all_required_params_present == True and response.query_result.action is not None:
	        jsonObj = MessageToJson(response.query_result)

                res["action"] = '{}|{}'.format(response.query_result.action,jsonObj)
                logging.info(res["action"])
                       
        return res

