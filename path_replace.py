#ファイル内の特定の文字列を置換したい

import glob

folder = "hoge" #相対パス書いて
Before_replacement = "hoge" #置換前文字列
After_replacement = "hoge" #置換後文字列

list = glob.glob(folder)#置換したいファイルが複数の場合でもリストで一括取得

for path in list:
    try:
        with open(path,"r",encoding="utf-8") as f:#読み取りでファイルを開く
            if f is None:#ファイルが見つからない時の処理
                print("missing file")
                import sys
                sys.exit()
            s = f.read()
        s = s.replace(Before_replacement,After_replacement)#文字列の変換　第一引数に元の文字列、第二引数に置換する文字列
        with open(path,"w",encoding="utf-8") as f:#書き込み用でフォルダを開く
            f.write(s)#ファイルに書き込み

    except:#例外処理
        import sys
        print("error",sys.exc_info()[0])
        print(sys.exc_info()[1])
        import traceback
        print(traceback.format_tb(sys.exc_info()[2]))

sys.exit()