import os
import sys
from watchlist import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
# 注意更新这里的路径，把 app.root_path 添加到 os.path.dirname() 中
# 以便把文件定位到项目根目录
SQLALCHEMY_DATABASE_URI = prefix + \
    os.path.join(os.path.dirname(app.root_path),
                 os.getenv('DATABASE_FILE', 'data.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
