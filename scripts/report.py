
import markdown

from text_type import TEXT_TYPE

def make_sample_md() -> str:
    sample_md: str = '''
## 前置き
- 個人調べなので、実はできる等あれば教えてください。

## 参考
- [Qiita マークダウン記法 一覧表・チートシート](https://qiita.com/kamorits/items/6f342da395ad57468ae3)

## 見出し
### できること
- h2, h3, h4, h5, h6は使用可能(このタイトルがh2)
### できないこと
- h1は使用不可
    - confluenceのAPI使用時にエラーになり投稿されない
- h7以降は存在が抹消される
### 実行例
## h2
### h3
#### h4
##### h5
###### h6

## リスト
### できること
- おそらく普通のmarkdownと変わらない
### 実行例
- リスト1
    - 子リスト
        - 孫リスト
            - 曾孫リスト
                - 玄孫リスト
- リスト2
- リスト3

## 番号付きリスト
### できること
- おそらく普通のmarkdownと変わらない
### 実行例
1. 1番目
    1. 1-1番目
        1. 1-1-1番目
            1. 1-1-1-1番目(ここまでやるな)
                1. 1-1-1-1-1番目(ここまでやるな)
                1. 1-1-1-1-2番目(ここまでやるな)
            1. 1-1-1-2番目(ここまでやるな)
        1. 1-1-2番目
    1. 1-2番目
1. 2番目

## 空行･改行･水平線
### できること
- たぶん何もできない。改行の仕様は普通のものと変わらないかも
### できないこと
- `<br>`は使用できない
- `_`は半角スペースにならない
- `---`は水平線にならない
### 実行例
1行目__（←半角スペース２つ）
2行目
3行目

## インライン表示
### できること
- たぶん普通のmarkdownと変わらない
### 実行例
`テキストやコード`

> 引用中ももちろん`できる`

## コード
### できること
- なんもできない
### できないこと
- そもそもコードとして入らない
- 言語指定のシンタックスハイライト
### 実行例
- markdownでは問題ないが、confluenceでは表記が崩れる。実行はできてしまう。
    - まあそもそもこの記法がGFMなので、pureなmarkdownでは書けないのだが。

```python
if (!lie) {
    return true;
}
```

## リンクの挿入
### できること
- たぶん普通のmarkdownと変わらない
### 実行例
Qiitaにアクセスしてみよう！[Qiita](http://qiita.com/)

## 引用
### できること
- たぶん普通のmarkdownと変わらない
### 実行例
> 引用してくれ

> 複数行
> もちろん
> できる

>> 2段目
>> もちろん
>> できる

>>> 3段目
>>> もちろん
>>> できる（やるな）

## 画像の挿入
### できること
- たぶん何もできない
    - 少なくともweb上の画像を引っ張ってくることはできない
    - もしかしたらconfluenceに画像をアップロードしたらできるかも。未確認
### できないこと
- 画像の挿入。つらい。
- 当然サイズ指定なども不可能。つらい。
### 実行例
- これがエラーになる。つらい。
`![qiita-square.png](https://qiita-image-store.s3.amazonaws.com/0/126861/90386757-fd96-8ba6-3477-485669713c55.png "qiita-square")`

## テーブル
### できること
- 普通のmarkdownと変わらない
    - ただし、pythonのmarkdown APIでextensionを指定する必要あり
### 実行例
| header1 | header2 | header3 |
|:-----------|------------:|:------------:|
| 左寄せ | 右寄せ | 中央寄せ |

## 文字
### できること
- 太字
### できないこと
- 斜体
- 文字色変更
- 打消し線
### 実行例
- **太字**にはなる
- *斜体*にはならない
- <font color="Red">赤色</font>にはならない
- ~~打消し線~~にもならない

## 注釈
### できること
- 何もできない
### できないこと
- 注釈そのもの
### 実行例
- 注釈[^1]の実行はできるが表示されない
[^1]: 注釈

    '''
    return sample_md

class Report: 
    def __init__(self):
        self.__md_text = None

    @property
    def md_text(self) -> None:
        return self.__md_text

    def make(self, text_type: TEXT_TYPE) -> str|None:
        if text_type not in TEXT_TYPE:
            raise NotImplementedError
        

        self.__md_text = make_sample_md()

        

        if text_type is TEXT_TYPE.MARKDOWN:
            return self.md_text
        elif text_type is TEXT_TYPE.HTML:
            # md = markdown.Markdown()
            # html = md.convert(self.md_text)
            html = markdown.markdown(self.md_text, 
                                     output_format='html', 
                                     extensions=['tables'])
            return html
        else:
            raise NotImplementedError
