# Language Model Playground

- [中文文件](#中文文件)
- [English](#English-Document)

## 中文文件

使用 PyTorch 實作 Language Model。

### 環境

1. Python 版本: 3.6+

2. CUDA 版本: 10.0+

### 安裝

1. 從 github 複製專案。

```sh
git clone https://github.com/ProFatXuanAll/language-model-playground.git
```

2. 移動到資料夾中。

```sh
cd language-model-playground
```

3. 安裝並啟動虛擬環境

```sh
# 使用 python3 內建提供的虛擬環境
# 如果無法執行請先安裝 `python3-dev` `python3-venv`
# 例如在 Ubuntu 上使用 `apt-get install python3-dev python3-venv`

# 如果使用 `conda` 請參考 `conda create --name venv python=3.6`
python3 -m venv venv # 安裝虛擬環境

# 如果使用 `conda` 請參考 activate venv
source venv/bin/active # 啟動虛擬環境
```

4. 安裝相依套件。

```sh
pip install -r requirements.txt
```

5. 新增資料夾 `data` 。

```sh
mkdir data
```

6. 從 kanews_collection.csv 上下載 [news_colleciton.csv](https://www.kaggle.com/ceshine/yet-another-chinese-news-dataset)，並解壓縮 `zip` 檔後把資料放到 `data/news_collection.csv`。

```sh
unzip yet-another-chinese-news-dataset.zip && chmod 666 news_collection.csv && mv news_collection.csv data/news_collection.csv
```

7. 訓練範例模型。

```sh
python run_train.py --experiment 1 --batch_size 32 --checkpoint -1 --checkpoint_step 500 --d_emb 100 --d_hid 300 --dataset news_collection_title --dropout 0.1 --epoch 10 --is_uncased --learning_rate 1e-4 --max_norm 1.0 --max_seq_len 60 --min_count 1 --model_class lstm --num_linear_layers 1 --num_rnn_layers 1 --optimizer_class adam --seed 42 --tokenizer_class char_dict
```

8. 使用 `tensorboard` 觀察模型誤差表現。

```sh
# 在 Windows 上路徑請用 `.\data\log`
tensorboard --logdir ./data/log
```

9. 指定訓練模型存檔點並生成範例句子。

```sh
# 使用第 500 步的存檔點進行句子生成
python run_generate.py --experiment 1 --checkpoint 500 --begin_of_sequence 今天 --beam_width 4 --max_seq_len 60
```

10. 評估模型在資料集上的 perplexity 表現。

```sh
# 使用第 500 步的存檔點進行表現評估
python run_perplexity_evaluation.py --experiment 1 --checkpoint 500 --dataset news_collection_title
```

11. 試著使用不同的超參數或更換模型並使用 `run_train.py` 重新訓練。接著使用 `run_generate.py` 給予相同 `begin_of_sequence` 進行生成並比較生成結果之不同。

### 開發

1. 請參考 [Google python style guide](https://google.github.io/styleguide/pyguide.html) 撰寫程式碼並使程式碼符合其風格。

2. 請參考 [`typing`](https://docs.python.org/3/library/typing.html) 為每個 `function` 與 `method` 加上型態註記。

3. 請為每個 `class`, `function` 與 `method` 補上 `docstring`。

4. 請執行 `pylint your_code.py` 自動驗證你的程式是否符合 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 的規範。

5. 請執行 `autopep8 -i -a -a your_code.py` 自動修改你的程式使其符合 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 的規範。

6. 請執行 `mypy your_code.py` 自動驗證程式碼的型別正確性。

7. 請執行 `python -m unittest` 確認程式碼是否通過單元測試。

8. 請撰寫單元測試程式碼讓程式碼容易維護。

## English Document

Language Model implemented with PyTorch.

### Environment

1. Python version: 3.6+

2. CUDA version: 10.0+

### Install

1. Clone the project.

```sh
git clone https://github.com/ProFatXuanAll/language-model-playground.git
```

2. Move to project directory

```sh
cd language-model-playground
```

3. Install and Launch Virtual Environment.

```sh
# Use python built-in virtual environment.
# The following script need `python3-dev` `python3-venv`.
# For example on Ubuntu use `apt-get install python3-dev python3-venv`.

# If you are using `conda` do `conda create --name venv python=3.6` instead.
python3 -m venv venv # Install virtual environment.

# If you are using `conda` do `activate venv` instead.
source venv/bin/active # Launch virtual environment.
```

4. Install Dependencies.

```sh
pip install -r requirements.txt
```

5. Create `data` folder.

```sh
mkdir data
```

6. Download [news_collection.csv](https://www.kaggle.com/ceshine/yet-another-chinese-news-dataset) from kaggle, extract from `zip` and put it at `data/news_collection.csv`.

```sh
unzip yet-another-chinese-news-dataset.zip && chmod 666 news_collection.csv && mv news_collection.csv data/news_collection.csv
```

7. Train example model.

```sh
python run_train.py --experiment 1 --batch_size 32 --checkpoint -1 --checkpoint_step 500 --d_emb 100 --d_hid 300 --dataset news_collection_title --dropout 0.1 --epoch 10 --is_uncased --learning_rate 1e-4 --max_norm 1.0 --max_seq_len 60 --min_count 1 --model_class lstm --num_linear_layers 1 --num_rnn_layers 1 --optimizer_class adam --seed 42 --tokenizer_class char_dict
```

8. Use `tensorboard` to observe model training loss performance.

```sh
# On Windows use path `.\data\log`
tensorboard --logdir ./data/log
```

9. Generate sequences using model checkpoints.

```sh
# Using checkpoint 500 to generate sequences.
python run_generate.py --experiment 1 --checkpoint 500 --begin_of_sequence 今天 --beam_width 4 --max_seq_len 60
```

10. Evaluate model performance on dataset by calculating perplexity.

```sh
# Using checkpoint 500 to evaluate.
python run_perplexity_evaluation.py --experiment 1 --checkpoint 500 --dataset news_collection_title
```

11. Try using different hyperparameters or change model, then use `run_train.py` to perform training as above example. Then run `run_generate.py` to compare generated results given exactly same `begin_of_sequence`.

### Development

1. Make sure your code conform [Google python style guide](https://google.github.io/styleguide/pyguide.html).

2. Do type annotation for every `function` and `method` (You might need to see [`typing`](https://docs.python.org/3/library/typing.html)).

3. Write `docstring` for every `class`, `function` and `method`.

4. Run `pylint your_code.py` to automatically check your code whether conform to [PEP 8](https://www.python.org/dev/peps/pep-0008/).

5. Run `autopep8 -i -a -a your_code.py` to automatically fix your code and conform to [PEP 8](https://www.python.org/dev/peps/pep-0008/).

6. Run `mypy your_code.py` to check type annotaions.

7. Run `python -m unittest` to perform unit tests.

8. Write unit tests for your code and make them maintainable.
