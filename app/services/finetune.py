from llama_index.finetuning import SentenceTransformersFinetuneEngine
from llama_index.core.evaluation import EmbeddingQAFinetuneDataset
from app import PROJECT_PATH, DATA_DIR, SYTHETIC_DATA_DIR
import os
import json

def finetuning(epochs, batch_size, evaluation_steps, model_id="BAAI/bge-m3",model_input_path=SYTHETIC_DATA_DIR, model_output_path="finetuned-bge-m3"):
    with open(os.path.join(model_input_path, 'train_dataset.json')) as json_data:
        dataset = json.load(json_data)
        train_dataset = EmbeddingQAFinetuneDataset(queries=dataset['queries'], 
                                                  corpus=dataset['corpus'],
                                                  relevant_docs=dataset['relevant_docs'])
        json_data.close()
    with open(os.path.join(model_input_path, 'val_dataset.json')) as json_data:
        dataset = json.load(json_data)
        val_dataset = EmbeddingQAFinetuneDataset(queries=dataset['queries'], 
                                                 corpus=dataset['corpus'],
                                                 relevant_docs=dataset['relevant_docs'])
        json_data.close()

    finetune_engine = SentenceTransformersFinetuneEngine(
        train_dataset,
        model_id=model_id,
        model_output_path=model_output_path,
        val_dataset=val_dataset,
        epochs=epochs,
        batch_size=batch_size,
        evaluation_steps=evaluation_steps
    )

    finetune_engine.finetune()

#finetuning(epochs=5, batch_size=2, evaluation_steps=7000)