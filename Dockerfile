# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存関係をコピー
COPY requirements.txt requirements.txt

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションをコピー
COPY . .

# ポート5000を開放
EXPOSE 5000

# Flaskを起動
CMD ["flask", "run", "--host=0.0.0.0"]
