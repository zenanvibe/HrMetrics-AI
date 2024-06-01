from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Add a padding token if not already present
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})

# fine tuned model stored in models/leave
model = AutoModelForCausalLM.from_pretrained("./models/leave")
model.resize_token_embeddings(len(tokenizer))

import torch

# Function to generate text based on a prompt
def generate_text(prompt, max_length=50):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(
        inputs.input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == '__main__':
    # Example prompt for testing
    prompt = "Context: hi|"
    generated_text = generate_text(prompt)
    print(generated_text)
