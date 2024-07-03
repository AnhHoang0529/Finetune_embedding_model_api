from . import api_blueprint
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import logging
import os
from llama_index.core import Settings
from app import PROJECT_PATH, SYTHETIC_DATA_DIR
from app.model.models import get_llm
from app.services.finetune import *

@api_blueprint.route('/ai/v1/llm/finetuning')
def upload():
            input = request.args.get('input')
            output = request.args.get('output')
            epoch = request.args.get('epoch')
            input_path = os.path.join(SYTHETIC_DATA_DIR, input)
            try:
                print(input_path)
                print(output)
                print(epoch)
                finetuning(epochs=ỉnt(epoch), batch_size=2, evaluation_steps=7000, model_input_path=input_path, model_output_path=output)
                print(jsonify({"success": True}))
                return jsonify({"success": True})
            except Exception as e:
                logging.exception(e)
                return jsonify({"success": False})
              

        

