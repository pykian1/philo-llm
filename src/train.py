from unsloth import FastLanguageModel
from datasets import load_dataset

model, tokenizer = FastLanguageModel.from_pretrained("mistralai/Mistral-7B-v0.1")
dataset = load_dataset("json", data_files="data/philosophy_dataset.jsonl")
#todo: add training code here
print("training script in progress")
