export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
datadir=./data/para
vocabdir=./data/vocab

modeldir=./saved_exp_model
mkdir -p $modeldir

rm -rf $modeldir/*

# batch_size is token level.
# infer_batch_size is example level.
python expert_model.py \
      --src=rapid.de \
      --tgt=rapid.en \
      --train_prefix=${datadir}/train \
      --dev_prefix=${datadir}/dev \
      --test_prefix=${datadir}/dev \
      --vocab_prefix=${vocabdir}/vocab \
      --max_vocab_size=120000 \
      --out_dir=${modeldir} \
      --optimizer=lazyadam \
      --warmup_steps=8000 \
      --learning_rate=2.1 \
      --num_train_steps=500000 \
      --steps_per_stats=100 \
      --steps_per_external_eval=1000 \
      --embedding_size=512 \
      --num_units=512 \
      --num_layers=2 \
      --ffn_inner_dim=512 \
      --batch_size=512 \
      --infer_batch_size=64 \
      --metrics=BLEU \
      --bucket_width=5 \
      --avg_ckpts=True \
      --label_smoothing=0.1 \
      --src_max_len=30 \
      --tgt_max_len=30 \
      --num_gpus=2

