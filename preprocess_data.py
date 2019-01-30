# We need to put all of training data into one txt document, as mentioned in the https://github.com/lovecambi/qebrain
# For now, we just using rapid for tasting and skip this part.

import os
import random

def generate_dev(base_path):
	# de_data_path = base_path + '/rapid2016.de-en.de'
	# en_data = base_path + '/rapid2016.de-en.en'

	# Here for DE data.
	de_sentences = []
	# count_de = 0
	with open(base_path + "rapid2016.de-en.de", 'r') as f:
		for line in f.readlines():
			# count_de += 1
			de_sentences.append(line)
	# print('count_de: ',count_de)
	print('length of DE data: ', len(de_sentences))
	# print('length of set(DE data): ', len(set(de_sentences)))

	# Here for EN data.
	en_sentences = []
	with open(base_path + "rapid2016.de-en.en", 'r') as f:
		for line in f.readlines():
			en_sentences.append(line)
	# print('count_en: ', count_en)
	# print('length of EN data: ', len(en_sentences))
	# print('length of set(EN data): ', len(set(en_sentences)))


	# to separate training set and dev set randomly.
	random.seed(23)
	dev_index = random.sample(range(len(de_sentences)), 100000)
	train_index = tuple(set(range(len(de_sentences))) - set(dev_index))
	de_devSet = [de_sentences[line] for line in dev_index]
	de_trainSet = [de_sentences[line] for line in train_index]
	print('length of de sev set: ', len(de_devSet))
	print('length of de training set: ', len(de_trainSet))
	# print(de_devSet[:5])

	en_devSet = [en_sentences[line] for line in dev_index]
	en_trainSet = [en_sentences[line] for line in train_index]
	print('length of de sev set: ', len(en_devSet))
	print('length of de training set: ', len(en_trainSet))
	# print(en_devSet[:5])

	# write training set and dev set into file.
	with open(base_path + "train.rapid.de", 'w') as f:
		for line in de_trainSet:
			f.write(line)
	# print('finished generating train for de')
	with open(base_path + "dev.rapid.de", 'w') as f:
		for line in de_devSet:
			f.write(line)
	# print('finished generating dev for de')
	with open(base_path + "train.rapid.en", 'w') as f:
		for line in en_trainSet:
			f.write(line)
	# print('finished generating train for en')
	with open(base_path + "dev.rapid.en", 'w') as f:
		for line in en_devSet:
			f.write(line)
	# print('finished generating dev for en')
	print('finished generating training set and dev set')


	# en_dev_index = random.sample(range(len(en_sentences)), 100000)
	# en_train_index = tuple(set(range(len(en_sentences))) - set(en_dev_index))
	# en_devSet = [en_sentences[line] for line in en_dev_index]
	# en_trainSet = [en_sentences[line] for line in en_train_index]
	# print('length of de sev set: ', len(en_devSet))
	# print('length of de training set: ', len(en_trainSet))
	# print(en_devSet[:5])


if __name__ == '__main__':
	para_data_path = './data/para/'
	generate_dev(para_data_path)