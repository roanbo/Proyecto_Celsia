from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class HuggingFaceModel:
    def __init__(self, model_name="jcortizba/modelo18"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return probabilities.tolist()

if __name__ == "__main__":
    model = HuggingFaceModel()
    text = "Este es un ejemplo de entrada."
    predictions = model.predict(text)
    print(f"Predicciones: {predictions}")
