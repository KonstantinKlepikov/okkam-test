# Okkam-test

## Task

Имеется дамп базы data.csv со следующими полями:

- `Date` – дата в формате `yyyymmdd`
- `respondent` – уникальный номер респондента
- `Sex` – пол респондента (1=М, 2=Ж)
- `Age` – возраст респондента
- `Weight` – Некая статистика респондента для этого дня

Необходимо:

1. Загрузить данные в таблицу СУБД SQL на ваш выбор (но не `SQLlite`)
2. Разработать API с одним `GET` эндпоинтом `/getPercent` который будет выполнять следующий алгоритм:

- На вход эндпоинта приходят 2 параметра: `audience1` и `audience2`:

- Аудитории будут приходить в формате SQL синтаксиса, например `Age BETWEEN 18 AND 35` или `Sex = 2 AND Age >= 18`
- Для каждой из аудиторий отобрать из таблицы всех респондентов, подходящих под параметры
- Для каждой из аудиторий взять средний Weight респондента этой аудиторий, сгруппировав по их уникальному номеру
- Далее вычислить процент вхождения второй аудитории в первую, основываясь на среднем Weight. Пример:

    - Имеем первую аудиторию, в которую входят resp1 с avg(Weight)=1, resp2 с avg(Weight)=2 и resp3 с avg(Weight)=3
    - Имеем вторую аудиторию, в которую входят resp2, resp3 и resp4 с avg(Weight) = 2,3,4 соответственно
    - Видим, что аудитории пересекаются респондентами resp2 и resp3, у которых avg(Weight) равен 2 и 3 (Средний Weight не может быть разным у одного и того же респондента). Значит процент вхождения второй аудитории в первую будет равен (2+3) / (1+2+3) = 0.8(3)

- Предусмотреть варианты:

    - Аудитории могут быть идентичными
    - Аудитории могут не пересекаться вообще
    - Вторая аудитория может быть подмножеством первой
    - Первая аудитория может быть подмножеством второй

- Отдать респонс в формате {‘percent’: результат}

3. Обернуть API в `Docker` контейнер
4. Подготовить `docker-compose` конфиг для связки API+СУБД:

- База данных должна быть создана и наполнена
- API слушает 80 порт

5. Опционально:

- Позаботиться об отказоустойчивости
- Позаботиться о быстродействии (учитывая, что данные не будут изменены ретроспективно)
- Порядок в коде – `pep8`, докстринги, тайпинг, структура проекта

## Run or stop stack from root

- `make serve` to run dev mode
- `make down` to stop

### Use local resources to watch project

- [api swagger docs](http://localhost:8100/docs/)
- [api redoc](http://localhost:8100/redoc/)

### Develop with each service

1. Go to service folder, f.e. `cd data-api/app` and create VSCode project by `code .`
2. Install poery dependencies and add environment for python linting. Use `poetry config virtualenvs.in-project true` for creation of env folder inside project. Then `poetry install --with dev`.
3. Inside container use:

    - `pytest -v -s -x` for all tests
    - use `python -m IPython` to check code
    - `mypy --install-types`
    - `mypy app` and `flake8 app`

## TO-DO

- [x] docker stack
- [ ] db models
- [ ] init dev db (dump)
- [ ] init and mock test db
- [ ] alembic migration
- [ ] pgadmin for vscode dev
- [ ] crud
- [ ] api models
- [ ] logic
- [ ] endpoint
- [ ] tests
- [ ] docs
