# Тестовое приложение lesta-test.

## Задание 1.

### Варианты запуска приложения:

1) ```git clone https://github.com/ilyaKrivitskiy/lesta-test.git```

    ```docker build -t lesta-test .```

    ```docker run -d -p {your_host_port|5000}:5000 lesta-test```,
    где {your_host_port|5000} - TCP порт локальной машины, например, 5000

    **Проверка приложения:**

    ```curl http://localhost:5000/ping```

2) ```docker login```

    ```docker pull me1vin/lesta-test```

    ```docker run -d -p 5000:5000 me1vin/lesta-test```

    **Проверка приложения:**

    ```curl http://localhost:5000/ping```
