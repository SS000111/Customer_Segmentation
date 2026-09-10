{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "9cde9747-985e-4472-9708-bd9cf48e1ea3",
      "cell_type": "markdown",
      "source": "<div style=\"background-color:  orange; padding: 15px; border-radius: 5px;\">\n    <h2>Phase 3 : Build Server app.ipynb</h2>\n    <p>To build Application User Interface.</p>\n\n* User to enter customer details to predict the respective customer segment as per training of the model\n  1. Inactive Customer\n  2. New Potential Customer\n  3. Highly Active Customer\n  4. Loyal Buyer\n</div>\n",
      "metadata": {}
    },
    {
      "id": "1c5d7bc2-524b-4dfe-8b20-bdf09f6e5726",
      "cell_type": "code",
      "source": "import numpy as np\nimport joblib\nimport os\nimport sklearn\nfrom flask import Flask, request, render_template\nfrom joblib import parallel_backend\napp = Flask(__name__)\n\nBASE_DIR = os.getcwd()\nMODEL_PATH = os.path.join(BASE_DIR, 'customer_segmentation_app/artifacts/hybrid_model.pkl')\n\nprint(f\"Loading Pipeline from: {MODEL_PATH}\")\n\ntry:\n    full_pipeline = joblib.load(MODEL_PATH)\n    print(\"Full Processing Pipeline Loaded.\")\nexcept Exception as e:\n    print(f\"CRITICAL ERROR: Could not load model.\\nDetail: {e}\")\n    full_pipeline = None\n\nSEGMENT_MAP = {\n    0: \"Highly Active Customer\",\n    1: \"Inactive Customer\",\n    2: \"Loyal Buyer\",\n    3: \"New Potential Customer\"\n}\n\n@app.route('/')\ndef home():\n    return render_template('index.html')\n\n@app.route('/predict', methods=['POST'])\ndef predict():\n    if not full_pipeline:\n        return render_template('index.html', prediction_text=\"Server Error: AI Brain missing.\")\n\n    try:\n        features = [\n            float(request.form['Age']),\n            float(request.form['Annual_Income']),\n            float(request.form['Spending_Score'])\n        ]\n        \n        input_vector = np.array([features])\n        \n        with parallel_backend('threading', n_jobs=1):\n            prediction_id = full_pipeline.predict(input_vector)[0]\n            \n        segment_name = SEGMENT_MAP.get(prediction_id, \"Unknown Segment\")\n        \n        return render_template('index.html', \n                             prediction_text=segment_name,\n                             input_data=features)\n\n    except Exception as e:\n        return render_template('index.html', prediction_text=f\"Calculation Error: {str(e)}\")\n\nif __name__ == \"__main__\":\n    app.run(debug=False,use_reloader=False,port=5000)",
      "metadata": {
        "trusted": True
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Loading Pipeline from: /drive/customer_segmentation_app/artifacts/hybrid_model.pkl\nFull Processing Pipeline Loaded.\n"
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": "Not supported\n"
        },
        {
          "ename": "<class 'SystemExit'>",
          "evalue": "1",
          "traceback": [
            "An exception has occurred, use %tb to see the full traceback.\n",
            "\u001b[31mSystemExit\u001b[39m\u001b[31m:\u001b[39m 1\n"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 18
    },
    {
      "id": "fcd3dc42-2632-4f46-9a23-e189eb71a54e",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": True
      },
      "outputs": [],
      "execution_count": None
    }
  ]
}
