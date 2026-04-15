# LLM FastAPI Project



## Описание



Серверное приложение на FastAPI с JWT-аутентификацией, SQLite и интеграцией с OpenRouter.



---



## Установка



```bash

uv init

uv venv

.venv\\Scripts\\activate



uv pip install -r <(uv pip compile pyproject.toml)

```



---



## Запуск



```bash

uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

```



---



## Аутентификация



### Регистрация



![request](./screenshots/request.png)



### Логин



![login](./screenshots/login.png)



### Авторизация (Swagger)



![auth](./screenshots/auth.png)



### Получение профиля



![auth_check](./screenshots/auth_check.png)



---



## Работа с чатом



### Запрос к LLM



![model_answer](./screenshots/model_answer.png)



### История пользователя



![history](./screenshots/history.png)



### Очистка истории



![delete_user](./screenshots/delete_user.png)





---



## Проверка кода



```bash

uv run ruff check

```



Результат:



![ruff_check](./screenshots/ruff_check.png)

