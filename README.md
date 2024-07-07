# Fine-tune Embedding Model API

This project provides a RESTful API for fine-tuning an embedding model using Flask. It includes endpoints for model fine-tuning and dataset generation. 

## Project Structure

```plaintext
Finetune_embedding_model_api/
├── environment.env
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py 
│   │   └── routes.py   
│   ├── model
│   │   └── model.py
│   ├── services
│   │   ├── finetune.py
│   │   └── generate_dataset.py
│   ├── utils     
│   │   └── prompt_templates.py
│   ├── data
│   │   └── json
│   ├── synthetic_data
│   │   └── qa_data
│   │       └── json
├── requirements.txt  
└── run.py
```

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/Finetune_embedding_model_api.git
    cd Finetune_embedding_model_api
    ```

2. **Create a virtual environment:**

    ```sh
    conda create -n finetune python=3.10
    conda activate finetune
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a file named `environment.env` in the root directory and add your environment variables.

## Usage

1. **Run the Flask application:**

    ```sh
    python run.py
    ```

2. **API Endpoints:**

    - `GET /ai/v1/llm/finetuning` - Endpoint for fine-tuning the model. Expects `input`, `output`, and `epoch` as query parameters.
      - `input`: The folder name containing generated data in QA form located in the `synthetic_data` folder.
      - `output`: The folder name where the fine-tuned model will be saved.
      - `epoch`: The number of epochs to use for fine-tuning (can be set between 1-5 epochs).

    Example:

    ```plaintext
    http://192.168.1.105:9000/ai/v1/llm/finetuning?input=qa_data&output=finetuned-bge-m3&epoch=1
    ```

## Project Components

- **app/__init__.py**: Initializes the Flask app and registers the blueprints.
- **app/api/routes.py**: Contains the API route definitions.
- **app/model/model.py**: Contains the embedding model logic.
- **app/services/finetune.py**: Contains the logic for fine-tuning the model.
- **app/services/generate_dataset.py**: Contains the logic for generating datasets.
- **app/utils/prompt_templates.py**: Contains utility functions and templates for prompts.
- **app/data/json**: Directory for storing data in JSON format.
- **app/synthetic_data/qa_data/json**: Directory for storing synthetic QA data in JSON format.
- **requirements.txt**: Lists the dependencies required for the project.
- **run.py**: The entry point for running the Flask application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Flask documentation
- Any other resources or libraries you used

---

Feel free to reach out if you have any questions or need further assistance!
