import json

json_string = '''
    {
      "students":[
        {
          "id": 1,
          "name": "Michael",
          "age": 1,
          "full-time": true
        },
        {
          "id": 2,
          "name": "Phillip",
          "age": 4,
          "full-time": false
        }
      ]
    }
'''
data = json.loads(json_string)
print(data['students'][0])

