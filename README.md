![](https://github.com/louceo/FSTR_sprint/blob/main/banner.png)
# Задача 
Федерация Спортивного Туризма России (ФСТР) заказала разработать мобильное приложение
для Android и IOS, которое упростило бы туристам задачу 
по отправке данных о перевале и сократило время обработки запроса до трёх дней. Моя "Backend" задача заключалась 
в создании REST API, который бы принимал и записывал данные в БД с соблюдением требований заказчика

# Требования к задаче 
- Создание БД
- Создание Метода submitData, который принимает JSON в теле запроса с информацией о перевале
- Написание REST API, который будет вызывать метод из класса по работе с данными
- Detail View (GET /submitData/<id>)
- Update View (PATCH /submitData/<id>)
- Отображать список данных обо всех объектах, которые пользователь с почтой email отправил на сервер (GET /submitData/?user__email=email)

# Tools 
- Django 4.1
- Django Rest Framework
- drf-writable-nested 
- drf_extra_fields 
- Swagger & OpenAPI

# Реализация 
Для Реализации REST API был выбран Django Rest Framework, а также несколько сторонних модулей: 
drf-writable-nested, drf_extra_fields, swagger & OpenAPI. Для тестирования были использованы:
Postman, Railway (Database Deployment).

## submitData View
![](https://github.com/louceo/FSTR_sprint/blob/main/submitData.png)
## Detail & Update View
![](https://github.com/louceo/FSTR_sprint/blob/main/detail_update.png)


