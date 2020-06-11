from typing import List

def sort_by_ext(files_list: List[str]) -> List[str]:
   name = []
   ext = []
   files = []
   for i in range(0, len(files_list)):
      if files_list[i].count('.') == 1:
         if files_list[i].index('.') == len(files_list[i])-1:
            name.append(files_list[i])
            ext.append('')
         elif files_list[i].index('.') == 0:
            name.append(files_list[i])
            ext.append('')
         else:
            a = files_list[i].split('.')
            name.append(a[0])
            ext.append(a[1])
            a.clear()
      elif files_list[i].count('.') > 1:
         if files_list[i][::-1].index('.') == 0:
            name.append(files_list[i])
            ext.append('')
         else:
            a = files_list[i][::-1].split('.', 1)
            name.append(a[1][::-1])
            ext.append(a[0][::-1])
      if files_list[i].count('.') == 0:
         name.append(files_list[i])
         ext.append('')
   for i in range(0, len(name)):
      files.append([name[i], ext[i]])
   files_list = files
   for i in range(0, len(files_list)):
      if files_list[i][0] == '':
         files_list[i][0] = files_list[i][1]
         files_list[i][1] = ''
         files_list[i][0] = '.' + files_list[i][0]
   files_list.sort(key=lambda files_list:files_list[0])
   files_list.sort(key=lambda files_list:files_list[1])
   result_list = []
   for i in range(0, len(files_list)):
      if files_list[i][1] == '':
         result_list.append(files_list[i][0])
      else:
         result_list.append(files_list[i][0] + "." + files_list[i][1])
   return result_list
if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['d.conf', 'a.bat']))
