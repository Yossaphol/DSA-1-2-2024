"""swap"""
def convert_string_to_tuples(text_in):
  """main"""
  values = text_in.strip('()').split(', ')
  return list(map(float, values))
laongdao_data = convert_string_to_tuples(input())
print((laongdao_data[1], laongdao_data[0]))