import torch


def generate_title(prompt, model,tokenizer, max_length=50,do_sample=True,):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones(input_ids.shape,dtype=torch.long)
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        # temperature=temperature,
        do_sample=do_sample,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id,
        num_return_sequences=1 
    )
    decode_output = tokenizer.decode(output[0], skip_special_tokens= True).strip()
    title = decode_output.split("\n")
    return title[0].strip()



  # Test
if __name__=="__main__":
    from transformers import GPT2Tokenizer, GPT2LMHeadModel

    # load model finetuning
    output_dir = "./fine_tuned_gpt2_generateTitle"
    model = GPT2LMHeadModel.from_pretrained(output_dir)
    tokenizer = GPT2Tokenizer.from_pretrained(output_dir)

    prompt = "Machine Learning"
    title = generate_title(prompt, model, tokenizer)
    print(f"Generated Title: {title}")