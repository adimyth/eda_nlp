# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou
from config import configs
from eda import *
import pandas as pd
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")


def gen_eda(data, text_col, label_col):
    sentences, labels = [], []
    for idx, row in tqdm(data.iterrows()):
        label = row[label_col]
        sentence = row[text_col]
        aug_sentences = eda(sentence, 
                            alpha_sr=configs.alpha_sr, 
                            alpha_ri=configs.alpha_ri, 
                            alpha_rs=configs.alpha_rs, 
                            p_rd=configs.p_rd,
                            num_aug=configs.num_aug)
        sentences.append(aug_sentences)
        labels.append([label]*len(aug_sentences))
    
    sentences = [j for sub in sentences for j in sub] 
    labels = [j for sub in labels for j in sub] 
    # strip & remove duplicates
    aug_data = pd.DataFrame({text_col: sentences, label_col: labels})
    aug_data[text_col] = aug_data[text_col].str.strip()
    aug_data = aug_data.drop_duplicates()
    return aug_data


if __name__ == "__main__":
    data = pd.read_csv("data/train.csv")
    print("Original DataFrame")
    print(f"Shape: {data.shape}\nSample: \n{data.head()}\n\n")

    aug_data = gen_eda(data, "text", "target", "id")
    aug_data = aug_data.drop_duplicates()
    print("Augmented DataFrame")
    print(f"Shape: {aug_data.shape}\nSample: \n{aug_data.head(10)}")
    aug_data.to_csv("data/train_augmented.csv", index=False)
