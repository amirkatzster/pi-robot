import sys
import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
from unittest.mock import ANY

sys.modules['dialogflow_v2'] = MagicMock()
import dialogflow_v2 as df
#from services.dialogflow import dialogflow


class test_dialogflow(unittest.TestCase):
    
    @unittest.mock.patch('dialogflow_v2.sessions_client')
    def test(self, sessions_client):
        self.assertEqual(3,3)
        # Arrange
        #res = MagicMock()
        # sessions_client =  MagicMock()
        # df.sessions_client = sessions_client
        # #mock.detect_intent(None,None)
        # #Act
        # res = dialogflow().detect_intent_texts(1,'hi')

        # #Assert
        # assert sessions_client.detect_intent.called


if __name__ == '__main__':
    unittest.main()