from transformers import GPT2Tokenizer,GPT2LMHeadModel,TextDataset,DataCollatorForLanguageModeling,TrainingArguments,Trainer
import accelerate

checkpoint = "gpt2"

tokenizer = GPT2Tokenizer.from_pretrained(checkpoint)
model = GPT2LMHeadModel.from_pretrained(checkpoint)

tokenizer.pad_token_id = tokenizer.eos_token_id

def load_data(file_path,tokenizer):
    return TextDataset(
        tokenizer = tokenizer,
        file_path = file_path,
        block_size = 128
        )

def load_data_collator(tokenizer):
    return DataCollatorForLanguageModeling(
        tokenizer = tokenizer,
        mlm = False,
    )



train_data = load_data("cleaned_arxiv_titles.csv",tokenizer)
data_collator = load_data_collator(tokenizer)


training_arguments = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2

)

trainer = Trainer(
    model=model,
    args=training_arguments,
    train_dataset=train_data,
    data_collator=data_collator
)


trainer.train()