# EE559 Mushroom Classification Project

Course project by **Ruiteng Li and Zhechao Zhao**, comparing baseline, logistic regression, multilayer perceptron, and Naive Bayes classifiers on mushroom data.

EE559 蘑菇分类课程项目，包含数据探索、预处理及多种分类模型的 Jupyter Notebook。

## Environment

The original project uses Python **3.12.11**. Create an isolated Python environment, then install the recorded dependencies:

```bash
python -m pip install -r requirements.txt
```

Open the notebooks in a compatible Jupyter environment. Paths are relative to the repository, so start it from the repository root.

## Suggested order

| Notebook | Purpose |
| --- | --- |
| [`data_exploration.ipynb`](data_exploration.ipynb) | Explore the dataset |
| [`data_preprocessing.ipynb`](data_preprocessing.ipynb) | Regenerate processed data if needed |
| [`baseline_model.ipynb`](baseline_model.ipynb) | Baseline classifier |
| [`logistic_regression.ipynb`](logistic_regression.ipynb) | Logistic regression |
| [`mlp.ipynb`](mlp.ipynb) | Multilayer perceptron |
| [`NaiveBayes1.1.ipynb`](NaiveBayes1.1.ipynb) | Naive Bayes experiment used by the original guide |

## Data

- [`raw_data/mushrooms.csv`](raw_data/mushrooms.csv): input data stored in the repository.
- [`preprocessed_data/processed_mushrooms.csv`](preprocessed_data/processed_mushrooms.csv): processed dataset identified by the original project guide.
- Other train/test CSVs and Naive Bayes notebooks are retained as experiment artifacts. Check each notebook's data-loading cells before comparing results.

Run the notebooks to reproduce their recorded workflow; no new model results or accuracy claims are asserted by this README.
