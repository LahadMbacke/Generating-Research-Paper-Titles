from finetuning import model,tokenizer
from scraping import fetch_arxiv_titles
from clean_data import clean_title
import torch
import pandas as pd


# scraping arxiv
titles = fetch_arxiv_titles()
df = pd.DataFrame(titles,columns=["titles"])
df.to_csv("arxiv_titles.csv",index=False)

# clean data
df = pd.read_csv("arxiv_titles.csv")
df['titles'] = df['titles'].apply(clean_title)
df.to_csv('cleaned_arxiv_titles.csv', index=False)




def generate_title(prompt, model,tokenizer, max_length=100):
    input = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones(input.shape,dtype=torch.long)
    output = model.generate(input, max_length=max_length,attention_mask=attention_mask,pad_token_id=tokenizer.pad_token_id, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens= True)

prompt = "RAG"
title = generate_title(prompt,model,tokenizer)

print(title)