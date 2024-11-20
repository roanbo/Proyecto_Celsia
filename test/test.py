import unittest
from src.main import HuggingFaceModel #main

class TestHuggingFaceModel(unittest.TestCase):
    def setUp(self):
        self.model = HuggingFaceModel()

    def test_predict_output(self):
        text = "Prueba de entrada."
        predictions = self.model.predict(text)
        self.assertIsInstance(predictions, list)
        self.assertGreater(len(predictions), 0)
        for prob in predictions[0]:
            self.assertGreaterEqual(prob, 0)
            self.assertLessEqual(prob, 1)

if __name__ == "__main__":
    unittest.main()