from urllib.parse import urlparse


def get_repo(git_link: str) -> str:
    """
    Функция возвращает названия репозитария из ссылки на github.

    >>> get_repo('https://github.com/username/reponame/')
    'reponame'
    """
    return urlparse(git_link).path.split('/')[2]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
