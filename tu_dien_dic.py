def find_and_print_word(data, input_word):

  for word, meaning in data.items():
    if word == input_word:
      print(f"Từ tiếng Việt của '{input_word}' là: {meaning}")
      break

data = {
  "hello": "xin chào",
  "goodbye": "tạm biệt",
  "thank you": "cảm ơn",
  "you're welcome": "không có gì",
}

input_word = input("Nhập từ tiếng Anh cần dịch: ")

translated_word = find_and_print_word(data, input_word)

