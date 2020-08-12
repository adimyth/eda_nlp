# EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks
[![Conference](http://img.shields.io/badge/EMNLP-2019-4b44ce.svg)](https://arxiv.org/abs/1901.11196)

This is the code for the EMNLP-IJCNLP paper [EDA: Easy Data Augmentation techniques for boosting performance on text classification tasks.](https://arxiv.org/abs/1901.11196) 

A blog post that explains EDA is [[here]](https://medium.com/@jason.20/these-are-the-easiest-data-augmentation-techniques-in-natural-language-processing-you-can-think-of-88e393fd610). 

By [Jason Wei](https://jasonwei20.github.io/research/) and Kai Zou.

Note: **Do not** email me with questions, as I will not reply. Instead, open an issue.

We present **EDA**: **e**asy **d**ata **a**ugmentation techniques for boosting performance on text classification tasks. These are a generalized set of data augmentation techniques that are easy to implement and have shown improvements on five NLP classification tasks, with substantial improvements on datasets of size `N < 500`. While other techniques require you to train a language model on an external dataset just to get a small boost, we found that simple text editing operations using EDA result in good performance gains. Given a sentence in the training set, we perform the following operations:

- **Synonym Replacement (SR):** Randomly choose *n* words from the sentence that are not stop words. Replace each of these words with one of its synonyms chosen at random.
- **Random Insertion (RI):** Find a random synonym of a random word in the sentence that is not a stop word. Insert that synonym into a random position in the sentence. Do this *n* times.
- **Random Swap (RS):** Randomly choose two words in the sentence and swap their positions. Do this *n* times.
- **Random Deletion (RD):** For each word in the sentence, randomly remove it with probability *p*.

<p align="center"> <img src="eda_figure.png" alt="drawing" width="400" class="center"> </p>
Average performance on 5 datasets with and without EDA, with respect to percent of training data used.

# Usage

You can run EDA any text classification dataset in less than 5 minutes. Just two steps:

### Install NLTK (if you don't have it already):

Pip install it.

```bash
pip install -U nltk
```

Download WordNet.
```bash
python
>>> import nltk; nltk.download('wordnet')
```

### Run EDA
To create an augmented version of your data, run `augment.py`. Simply change, the file name to load inside `__main__` function & specify - *text* & *label* column names.

In a change from the original implementation at - https://github.com/jasonwei20/eda_nlp. I've created a `config.py` file to specify the `alpha` values for each of the 4 augmentation techniques as well as `num_aug`.

```python
* alpha_sr - percentage of word to apply synonym replacement in a sentences
* alpha_ri - percentage of word to apply random insertion in a sentences
* alpha_rs - percentage of word to apply random swap in a sentences
* p_rd - probability of a word being randomly deleted
* num_aug - number of augmentations to apply
```

Inside, `augment.py` run the `gen_eda` function. It accepts the following parameters - 
* `data` - Dataframe containing text and label
* `text_col` - Column containing sentences
* `label_col` - Label column 

Best of luck!

# Citation
If you use EDA in your paper, please cite us:
```
@inproceedings{wei-zou-2019-eda,
    title = "{EDA}: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks",
    author = "Wei, Jason  and
      Zou, Kai",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1670",
    pages = "6383--6389",
    abstract = "We present EDA: easy data augmentation techniques for boosting performance on text classification tasks. EDA consists of four simple but powerful operations: synonym replacement, random insertion, random swap, and random deletion. On five text classification tasks, we show that EDA improves performance for both convolutional and recurrent neural networks. EDA demonstrates particularly strong results for smaller datasets; on average, across five datasets, training with EDA while using only 50{\textbackslash}{\%} of the available training set achieved the same accuracy as normal training with all available data. We also performed extensive ablation studies and suggest parameters for practical use.",
}
```

# Experiments

The code is not documented, but is [here](https://github.com/jasonwei20/eda_nlp/tree/master/experiments) for all experiments used in the paper. See [this issue](https://github.com/jasonwei20/eda_nlp/issues/10) for limited guidance.



