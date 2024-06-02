# Как запустить на ПК

Выбираем, куда будем кланировать (например на диск B в папку TEST_PROJECT)

```bash
cd /B/TEST_PROJECT
```

Клонируем проект:

```bash
git clone https://github.com/Vettel12/api_yatube-master
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```

Для запуска тестов выполним:

```bash
pytest
```

Получим:

```bash
tests/test_auth.py::TestAuthAPI::test_auth PASSED                                                                                               [  6%]
tests/test_comment.py::TestPostAPI::test_comments_not_found PASSED                                                                              [ 13%]
tests/test_comment.py::TestPostAPI::test_comments_get PASSED                                                                                    [ 20%]
tests/test_comment.py::TestPostAPI::test_comments_create PASSED                                                                                 [ 26%]
tests/test_comment.py::TestPostAPI::test_post_get_current PASSED                                                                                [ 33%]
tests/test_comment.py::TestPostAPI::test_post_patch_current PASSED                                                                              [ 40%]
tests/test_comment.py::TestPostAPI::test_post_delete_current PASSED                                                                             [ 46%]
tests/test_post.py::TestPostAPI::test_post_not_found PASSED                                                                                     [ 53%]
tests/test_post.py::TestPostAPI::test_post_not_auth PASSED                                                                                      [ 60%]
tests/test_post.py::TestPostAPI::test_posts_get PASSED                                                                                          [ 66%]
tests/test_post.py::TestPostAPI::test_post_create PASSED                                                                                        [ 73%]
tests/test_post.py::TestPostAPI::test_post_get_current PASSED                                                                                   [ 80%]
tests/test_post.py::TestPostAPI::test_post_patch_current PASSED                                                                                 [ 86%]
tests/test_post.py::TestPostAPI::test_post_delete_current PASSED                                                                                [ 93%]
tests/test_auth.py::TestAuthAPI::test_settings PASSED                                                                                           [100%] 

================================================================= 15 passed in 8.39s ================================================================= 
```

Создать суперпользователя:

```bash
python manage.py createsuperuser
```

Запустить проект:

```bash
python manage.py runserver
```

# Примеры запросов API в Postman

Получить токен по (POST) запросу: http://127.0.0.1:8000/api/v1/api-token-auth/

Для получения токена надо ввести username и password (которые вы ранее создали для суперпользователя)

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20210358+.png?raw=true" align="center" alt="GitHub Readme Stats" />

Получить спискок публикаций (GET): http://127.0.0.1:8000/api/v1/posts/

Ввести в Authorization наш token e233213*****

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20214854+.png?raw=true" align="center" alt="GitHub Readme Stats" />

Создать публикацию (GET): http://127.0.0.1:8000/api/v1/posts/

Ввести text и в Value наш текст поста

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20214936.png?raw=true" align="center" alt="GitHub Readme Stats" />

Обновление публикации (PUT): http://127.0.0.1:8000/api/v1/posts/1/

Ввести text и в Value новый текст

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20220142.png?raw=true" align="center" alt="GitHub Readme Stats" />

Удалить пост (ранее создали их три) (DELETE): http://127.0.0.1:8000/api/v1/posts/3/

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20220502.png?raw=true" align="center" alt="GitHub Readme Stats" />

Создать комментарий к посту (POST): http://127.0.0.1:8000/api/v1/posts/1/comments/

Ввести post и в Value его id

Ввести text и в Value значение

<img width="1000px" src="https://github.com/Vettel12/api_yatube-master/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-05-30%20215844.png?raw=true" align="center" alt="GitHub Readme Stats" />