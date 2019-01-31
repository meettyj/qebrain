# qebrain_GPU-Test

This repository is forked from [lovecambi/qebrain](https://github.com/lovecambi/qebrain) and provides a quick GPU running test. In the paper ["Bilingual Expert" Can Find Translation Errors](https://arxiv.org/abs/1807.09433), which proposed the qebrain, the author has trained the model on 8 Nvidia P-100 GPUs with 16 GB memory each for about 3 days until convergence. However, it may be challenging for us to have such computing resource. Thus, a quick experiment need to be done to find out the actual running time, or, whether it can be running or not.

## Requirements
1. TensorFlow 1.12 `pip install tensorflow-gpu`
2. OpenNMT-tf 1.15 `pip install OpenNMT-tf`
We used the following OpenNMT-tf APIs, so the latest OpenNMT-tf may also work if they are not changed. OpenNMT-tf also claimed backward compatibility guarantees.
    * `encoders.self_attention_encoder.SelfAttentionEncoder`
    * `layers.position.SinusoidalPositionEncoder`
    * `decoders.self_attention_decoder.SelfAttentionDecoder`
    * `utils.losses.cross_entropy_sequence_loss`
    * `encoders.BidirectionalRNNEncoder`
    * `layers.ConcatReducer`

## Basic Usage
1. Download the [rapid2016 parallel datasets](http://data.statmt.org/wmt18/translation-task/rapid2016.tgz) and extract it into folder `data/para` (two emtpty files rapid2016.de-en.de(en) for representative purpose). You can also find other parallel dataset in [WMT website.](http://www.statmt.org/wmt18/translation-task.html#download) 
2. Run `python preprocess_data.py` to randomly separate training set and dev set. After that we should have parllel data appeared in folder `data/para` (like we show with four other empty files). 
3. Run `./expert_train.sh` to train bilingual expert model, and due to the large dataset, we provide the multi GPU implementation.
4. Download the [QE dataset](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2619). An example dataset of sentence level De-En QE task has been downloaded and preprocessed in folder `data/qe`, including human features (If no human feature is prepared, set the argument `--use_hf=False`). 
5. Run `./qe_train.sh` to train the quality estimation model, and due to the small dataset, we only provide the single GPU implementation.
6. Run `./qe_infer.sh` to make the inference on dataset without labels.

Reminds: If you are using rapid2016 dataset for quick test, you do not need to generate vocabulary agagin, because we contained it in folder `data/vocab`. Otherwise, you need run `python generate_vocab.py` to generate vocabulary file. 

## Suggestions
I failed (memory limitations) running qebrain in my GPUs (2 * GTX 1080 Ti with 12GB memory each), and I have tried so many different sets of hparams (embedding_size, num_units, ffn_inner_dim, batch_size). Still cannot make it. So if you guys have less memory than 24 GB, it would be a good choice to skip it. Otherwise you can ignore me and give it a brave try. Do not forget I already have done some part in data preprocessing and it would be free for you to move on. Anyway, if you find this repo helpful, I appreciate you can give it a star. Good luck warrior.
