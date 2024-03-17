def dem_so_lan_xuat_hien(van_ban):

  num_words = {}
  text_list = van_ban.split()
  for word in text_list:
    word = word.lower().strip()
    so_lan_xuat_hien = num_words.get(word, 0)
    num_words[word] = so_lan_xuat_hien + 1
  return num_words

message = "If you know how you going to die , will you live diffrently ?"

so_lan_xuat_hien_cua_tu = dem_so_lan_xuat_hien(message)

for word, count in so_lan_xuat_hien_cua_tu.items():
  print(f"Từ '{word}' xuất hiện {count} lần.")