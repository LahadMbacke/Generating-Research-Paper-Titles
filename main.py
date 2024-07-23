from finetuning import model,tokenizer
from scraping import 
import torch






def generate_title(prompt, model,tokenizer, max_length=50):
    input = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones(input.shape,dtype=torch.long)
    output = model.generate(input, max_length=max_length,attention_mask=attention_mask,pad_token_id=tokenizer.pad_token_id, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens= True)

prompt = "Depp Learning in"
title = generate_title(prompt,model,tokenizer)

print(title)