cd OLMo
torchrun --nproc_per_node=8 scripts/train.py ../train_configs/FoPE_60M.yaml
