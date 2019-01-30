import os
# import pickle

def generate_vocab(base_path):
    en_out_path = "./data/vocab/vocab.rapid.en"
    de_out_path = "./data/vocab/vocab.rapid.de"

    # Here for DE data.
    de_sentences = []
    with open(base_path + "rapid2016.de-en.de", 'r') as f:
        for line in f.readlines():
            # desc = line.strip().split('\t')
            item = line.split()
            de_sentences.extend(item)

    de_vocab = set(de_sentences)
    print("de_vocab", len(de_vocab), "de_origin_vocab", len(de_sentences))

    with open(de_out_path, 'a') as de_f:
        de_f.write('<blank>'+ '\n'+'<s>'+'\n'+'</s>'+'\n')
        for _, word in enumerate(de_vocab):
            de_f.write(word + '\n')
        de_f.write('<unk>' + '\n')
    print('finished generating de vocabulary')


    # Here for EN data.
    en_sentences = []
    with open(base_path + "rapid2016.de-en.en", 'r') as f:
        for line in f.readlines():
            # desc = line.strip().split('\t')
            item = line.split()
            en_sentences.extend(item)

    en_vocab = set(en_sentences)
    print("en_vocab", len(en_vocab), "en_origin_vocab", len(en_sentences))

    with open(en_out_path, 'a') as en_f:
        en_f.write('<blank>'+ '\n'+'<s>'+'\n'+'</s>'+'\n')
        for _, word in enumerate(de_vocab):
            en_f.write(word + '\n')
        en_f.write('<unk>' + '\n')
    print('finished generating en vocabulary')


if __name__ == '__main__':
    # you can add more path here for vocabulary generating.
    rapid_path = "../data/rapid2016/"

    path_list = [rapid_path]
    for i in range(len(path_list)):
        generate_vocab(path_list[i])