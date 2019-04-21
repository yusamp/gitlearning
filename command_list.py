# -*- coding: utf-8 -*-
# [gitの開始(ルートフォルダで行う)]
# git init
#
# [gitインデックスへ追加]
# -単体
#  git add ファイル名
# -直下フォルダ全て
#  git add .
#
# [gitリポジトリへ追加]
# git commit -m "commitメッセージ"
#
# [commitログの確認]
# git log [--oneline]
#
# [commit同士の差分を取る(IDは7桁で充分)]
# git diff ID ID
#
# [IDの状態に復元]
# git checkout ID
#
# [Authorの登録]
# git config global user.name "名前"
# git config global user.email メールアドレス
#
# [直前のcommitを現在登録されているAuthorに変更]
# git commit --amend --reset-author
#
# [addとcommitを同時に行う]
# git commit -a -m "コミットメッセージ"
# *既にindexにあるもののみなので新規作成ファイルには行えない
#
# [indexに追加されたファイルを除外する]
# git reset HEAD ファイル名
#
# [全ての変更をHEADに戻す]
# git reset --hard HEAD
#
# [HEADの状態にファイルを戻す]
# git checkout HEAD ファイル名
#
# [直前のcommitを上書きする]
# git commit --amend
#
# [インデックスにあるファイルを削除する]
# git rm ファイル名
#
# [ファイル名の変更のみ]
# git mv 変更前ファイル名 変更後ファイル名
