#!/bin/bash

if [ "$1" = "train" ]; then
        echo "start to train......"

        CUDA_VISIBLE_DEVICES=0,1 python ../scene_classifier/fix_2_train.py \
                                    --vocab_file /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/vocab.txt    \
                                    --bert_config_file /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/bert_config.json   \
                                    --do_lower_case    \
                                    --train_file /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/data.train \
                                    --eval_train_file  /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/train_data.dev  \
                                    --eval_file  /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/data.dev   \
                                    --train_batch_size 32   \
                                    --eval_batch_size 32 \
                                    --learning_rate 2e-5   \
                                    --num_train_epochs 3   \
                                    --top_n 5   \
                                    --max_seq_len 150 \
                                    --num_labels 2   \
                                    --output_dir ../models/5_scene_model_bert_fix2 \
                                    --bert_model /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese   \
                                    --init_checkpoint /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/pytorch_model.bin   \
                                    --do_train   \
                                    --gradient_accumulation_steps 1 # 3>&2 2>&1 1>&3 | tee logs/3_scene_model0521_bert.log


elif [ "$1" = "eval" ];then
        echo "start to eval......"

        CUDA_VISIBLE_DEVICES=0,1 python ../scene_classifier/fix_3_train.py \
                                    --vocab_file /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/vocab.txt    \
                                    --bert_config_file /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/bert_config.json   \
                                    --do_lower_case    \
                                    --train_file /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/small.data.train \
                                    --eval_train_file  /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/small.train_data.dev  \
                                    --eval_file  /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/data.dev   \
                                    --train_batch_size 20   \
                                    --eval_batch_size 20 \
                                    --learning_rate 1e-5   \
                                    --num_train_epochs 6   \
                                    --top_n 3   \
                                    --num_labels 2   \
                                    --output_dir ./3_scene_model0525_bert \
                                    --result_file ./3_scene_model0525_bert/top5_predict_0525.csv    \
                                    --bert_model /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese   \
                                    --init_checkpoint /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/pytorch_model.bin   \
                                    --do_predict   \
                                    --gradient_accumulation_steps 1 3>&2 2>&1 1>&3 | tee logs/3_scene_model0521_bert.log

elif [ "$1" = "predict" ];then
        echo "start to predict......"

        CUDA_VISIBLE_DEVICES=7,4 python ../scene_classifier/fix_2_train.py \
                                    --vocab_file /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/vocab.txt    \
                                    --bert_config_file /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/bert_config.json   \
                                    --do_lower_case    \
                                    --train_file /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/small.data.train \
                                    --eval_train_file  /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/small.train_data.dev  \
                                    --eval_file  /nas/xd/projects/novel_analyzer/scene_cut_datas/0527/small.data.dev   \
                                    --predict_file /nas/xd/data/kuaidian/clear_kuaidian_0519/高冷校草缠上我.txt \
                                    --train_batch_size 20   \
                                    --eval_batch_size 20 \
                                    --learning_rate 1e-5   \
                                    --num_train_epochs 6   \
                                    --top_n 5   \
                                    --num_labels 2   \
                                    --output_dir /nas/lishengping/scene_models/5_scene_model0525_bert \
                                    --result_file /nas/lishengping/scene_models/5_scene_model0525_bert/predict.csv    \
                                    --bert_model /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese   \
                                    --init_checkpoint /nas/pretrain-bert/pretrain-pytorch/bert-base-chinese/pytorch_model.bin   \
                                    --do_predict   \
                                    --gradient_accumulation_steps 1 3>&2 2>&1 1>&3 | tee logs/5_scene_model0526_bert.log
else
    echo 'unknown argment 1'
fi

