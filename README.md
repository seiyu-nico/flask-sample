# django

## アプリケーションを追加するとき
- プロジェクトルートにアプリを作成すると、名前によってconfigの上下に来てしまうのでappsディレクトリを作成し、その中に各アプリを作成
```
mkdir apps
cd apps && python ../manage.py startapp hoge && cd ..
```

## Webの起動
```
python app.py
```

## CLIの起動
```
export FLASK_APP=cli.py
flask commands --help
flask commands ham
flask commands spam
```
