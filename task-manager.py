#リストの作成
tasks = []

while True:
  print("\n1: 追加")
  print("2: 一覧")
  print("3: 削除")
  print("4: 終了")

  choice = input("番号を選択してください：")

  if choice == "1":
    #追加
    task_name = input("追加するタスク名: ")
    tasks.append(task_name)
    print(task_name, "を追加しました")

  elif choice == "2":
    #一覧
    for i, name in enumerate(tasks, 1):
      print(i,":", name)

  elif choice == "3": 
    #削除
    try:
      task_num = int(input("削除するタスク番号: "))
      if 1 <= task_num <= len(tasks):
        deleted_task = tasks[task_num -1]
        tasks.pop(task_num-1)        
        print(f"{task_num}: {deleted_task}　を削除しました")
      else:
        print("その番号はありません")
    except ValueError:
      print("数字を入力してください")

  elif choice == "4":
    #終了
    print("終了します")
    break
  else:
    print("無効な選択です")
