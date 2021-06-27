from ../tododb import TodoDB
from slackbot.bot import respond_to

@respond_to(r'^todo:\s+add\s+(\S+)\s+(\S+)')
def add(message, title, limit_at):
  todo_tabel = TodoDB()
  todo_table.add(title, limit_at)
  message.reply(get_todo_list())

@respond_to(r'^todo:\s+delete\s+(\d+)')
def delete(message, todo_id):
  todo_table = TodoDB()
  todo_table.delete(todo_id = int(todo_id))
  message.reply(get_todo_list())
  
def get_todo_list():
  todo_table = TodoDB()
  todo_list = todo_table.all()
  msg = ""
  for item in todo_list:
    msg += item.id + ": " + item.title + ": " + item.limit_at + "\n"
  return msg
