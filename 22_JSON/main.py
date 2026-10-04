# 🔰🔰 JSON (JavaScript Object Notation)

import json

# ⚡ Mengonversi JSON ke Python

# json_data = "{'nama': 'John', 'usia': 30, 'kota': 'New York'}" error karena 
# menggunakan tanda kutip tunggal

json_data = '{"nama": "John", "usia": 30, "kota": "New York"}'
python_data = json.loads(json_data)
print('Data Python:', python_data)

# ⚡ Mengonversi Python ke JSON

python_data = {
    "nama": "Jane", 
    "usia": 25,
    "kota": "Los Angeles"
}
json_data = json.dumps(python_data)
print('Data JSON:', json_data)

# 🔖 mengkonversi objek python deng beberapa 
# tipe data ke JSON

print('LIST ke JSON:', json.dumps([1, 2, 3, 4, 5]), 'type >>>', type(json.dumps([1, 2, 3, 4, 5]))) 
print('TUPLE ke JSON:', json.dumps((1, 2, 3, 4, 5)), 'type >>>', type(json.dumps((1, 2, 3, 4, 5)))) 
print('DICT ke JSON:', json.dumps({"nama": "Alice", "usia": 28}), 'type >>>', type(json.dumps({"nama": "Alice", "usia": 28})))
print('BOOL ke JSON:', json.dumps(True), 'type >>>', type(json.dumps(True)))
print('FLOAT ke JSON:', json.dumps(3.14), 'type >>>', type(json.dumps(3.14)))
print('INT ke JSON:', json.dumps(42), 'type >>>', type(json.dumps(42)))
print('NONE ke JSON:', json.dumps(None), 'type >>>', type(json.dumps(None)))

# konversi objek python yang berisi semua tipe data yang sah

objekDataSah = {
    "nama": "Bob",
    "usia": 35,
    "sudahMenikah": False,
    "anak": None,
    "hobi": ["belajar", "mendengar musik"],
    "bahasa": ('python', 'javascript'),
    "pendidikan": {'SD': 'SDN01', 'SMP': 'SMPN01', 'SMA': 'SMAN01', 'ST':'Teknik Infromatika'}
}

print('-------------')
print(json.dumps(objekDataSah))
print('-------------')  

# ⚡ Memformat String JSON

print(json.dumps(objekDataSah, indent= 2))
print('-------------')  
print(json.dumps(objekDataSah, indent= 2, separators= ('--', '::')))
print('-------------')  
print(json.dumps(objekDataSah, indent= 2, sort_keys= True))

