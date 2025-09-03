from transformers import pipeline

model_path = "./philosophy_lora" #post trainining
pipe = pipeline("text-generation", model=model_path)
print(pipe("What is justice?", max_length=100)[0]["generated_text"])

