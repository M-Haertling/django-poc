```
python manage.py runserver
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/persons/
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/persons/?name=Mike
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/persons/?name=Wendy

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name": "Wendy","email": "wendy@gmail.com"}' \
  http://127.0.0.1:8000/api/persons/

curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"name": "Wendy","email": "wendy-revised@gmail.com"}' \
  http://127.0.0.1:8000/api/persons/

curl --request DELETE http://127.0.0.1:8000/api/persons/?name=Wendy

```

todo

pip install drf-excel
https://www.django-rest-framework.org/api-guide/renderers/#microsoft-excel-xlsx-binary-spreadsheet-endpoints

https://www.django-rest-framework.org/api-guide/renderers/#csv