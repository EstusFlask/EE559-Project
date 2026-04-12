import subprocess

process = subprocess.run(
    ["pigar", "gen", "."],
    input="y\nscikit-learn\n",  # 自动回答
    text=True
)