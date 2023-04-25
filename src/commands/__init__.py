from flask.cli import AppGroup
from commands.ham import handler as ham_handler
from commands.spam import handler as spam_handler

# グループを作成
commands = AppGroup('commands')

# task関連のコマンドを追加していく
commands.add_command(ham_handler)
commands.add_command(spam_handler)
