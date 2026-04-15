class AppError(Exception):
    """Базовая доменная ошибка приложения."""


class ConflictError(AppError):
    """Конфликт данных, например email уже существует."""


class UnauthorizedError(AppError):
    """Ошибка аутентификации."""


class ForbiddenError(AppError):
    """Недостаточно прав."""


class NotFoundError(AppError):
    """Объект не найден."""


class ExternalServiceError(AppError):
    """Ошибка внешнего сервиса."""