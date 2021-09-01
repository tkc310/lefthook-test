## lefthook install

```bash
$ brew install lefthook

# .git/hook/pre-commitに反映
$ lefthook install
$ lefthook add pre-commit

# pre-commitを実行(commitの有無に関わらず施行できる)
$ lefthook run pre-commit
```

## Use GUI git client

```bash
# CUI経由でGUIを起動
$ open /Applications/Tower.app

# GUI用にPATHを通す (環境変数を読み込む)
$ touch ~/.lefthookrc
$ echo 'source ~/.bash_profile' >> ~/.lefthookrc
```
