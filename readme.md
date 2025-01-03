### quick setup
git clone https://github.com/KT313/base_llm_training_setup --recursive
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_dev.txt
wandb login

python3 download_data.py

torchrun OLMo/scripts/train.py train_configs/CONFIG_TO_RUN.yaml

wget "https://huggingface.co/allenai/gpt-neox-olmo-dolma-v1_5/resolve/main/tokenizer.json?download=true" -O "workspace/PROJECT_NAME/tokenizer.json"
python3 OLMo/scripts/convert_olmo_to_hf_new.py --input_dir workspace/PROJECT_NAME/latest-unsharded --output_dir workspace/PROJECT_NAME/latest-hf --tokenizer_json_path workspace/PROJECT_NAME/tokenizer.json --safe_serialization true