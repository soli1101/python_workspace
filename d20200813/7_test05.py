from pathlib import Path

Path("./img/test").mkdir(exist_ok=True) 
# 저 디렉토리가 있으면 됐고 없으면 만들어
Path("./img/aaa/bbb/ccc/test").mkdir(parents=True, exist_ok=True) 
# 만약 그 부모 디렉토리도 없으면 다 만들어  