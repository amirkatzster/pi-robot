import os
import dialogflow_v2 as df
from services.actionHandler import actionHandler

class dialogflow:
    
    project_id = os.environ['DIALOG_FLOW_PROJECT_ID']
    language_code = 'en-US'

    # detect_intent_texts('1',['How old are you?'])
    def detect_intent_texts(self, session_id, texts):
        """Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversaion."""
        session_client = df.SessionsClient()

        session = session_client.session_path(self.project_id, session_id)
        print('Session path: {}\n'.format(session))

        fulfillemnts = []
        for text in texts:
            # pylint: disable=E1101
            text_input = df.types.TextInput(
                text=text, language_code=self.language_code)

            query_input = df.types.QueryInput(text=text_input)

            response = session_client.detect_intent(
                session=session, query_input=query_input)

            print('=' * 20)
            print('Query text: {}'.format(response.query_result.query_text))
            print('Detected intent: {} (confidence: {})\n'.format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence))
            print('Fulfillment text: {}\n'.format(
                response.query_result.fulfillment_text))
            fulfillemnts.append(response.query_result.fulfillment_text)
            if response.query_result.all_required_params_present == True and response.query_result.action is not None:
               actionHandler().process(response.query_result.action,response.query_result.parameters)
               
               
        return fulfillemnts

