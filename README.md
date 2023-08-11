# AtCoder for Python

## 特徴

- [atcoder-cli](https://github.com/Tatamo/atcoder-cli)と[oj](https://github.com/online-judge-tools/oj)を用いた解答用ファイル生成、ローカルでのテストケースチェック、提出
- [poethepoet](https://github.com/nat-n/poethepoet)による共通化されたコマンドの提供

## 導入

- Python環境の構築
  - おすすめは[asdf](https://asdf-vm.com/)による環境構築
  - AtCoder環境に合わせて、3.8系にしておくのが良し
  ```
  # asdfの場合
  asdf plugin-add python
  asdf install python 3.8.17
  ```
- [Poetry](https://github.com/python-poetry/poetry)の導入
  ```
  # 通常のインストール
  curl -sSL https://install.python-poetry.org | python3 -

  # asdfの場合
  asdf plugin-add poetry
  asdf install poetry latest
  asdf global poetry latest
  ```
- [pipx](https://github.com/pypa/pipx)の導入
  ```
  # 通常のインストール
  ## for macOS
  brew install pipx
  ## for Linux
  python3 -m pip install --user pipx

  # asdfの場合
  asdf plugin-add pipx
  asdf install pipx latest
  asdf global pipx latest
  ```
- [poethepoet](https://github.com/nat-n/poethepoet)の導入
  ```
  pipx install poethepoet
  ```
- Node.jsとnpm/yarnの導入
- [atcoder-cli](https://github.com/Tatamo/atcoder-cli)の導入
  ```
  # yarnの場合
  yarn global add atcoder-cli
  # npmの場合
  npm install -g atcoder-cli
  ```

# 初期設定

- リポジトリをクローンし、ディレクトリ内に移動
  - GitHub上で`Use this template`で自身のリポジトリを作成してからクローンがおすすめ
- 依存ライブラリのインストール
  ```
  poetry install
  ```
- atcoder-cliのログイン
  ```
  acc login
  ```
- ojのログイン
  ```
  poetry run oj login https://atcoder.jp/
  ```
- 解答用テンプレートファイルの設定
  - 以下のコマンドで設定ファイルのディレクトリに移動
    ```
    cd $(acc config-dir)
    ```
  - `config.json`を以下のように修正
    - "default-task-choice": "all"
    - "default-template": "python"
  - 同一ディレクトリに`python`フォルダを作成
  - `python`フォルダ内に以下の2ファイルを作成
    - `main.py`: こちらのファイルがコピーされるので、自分が使いやすい形に変更すると良い
      ```
      def main():
          pass

      main()
      ```
    - `template.json`
      ```json
      {
        "task": {
          "program": [
            "main.py"
          ],
          "submit": "main.py"
        }
      }
      ```

# 使い方

- プロジェクトのディレクトリに移動して実行

## コンテスト用解答ファイルの生成 (`new`)

```
poe new [contestID]
```

## テストケースのローカルチェック (`test`)

```
poe test [contestID] [taskID]
```

## 提出 (`submit`)

```
poe submit [contestID] [taskID]
```