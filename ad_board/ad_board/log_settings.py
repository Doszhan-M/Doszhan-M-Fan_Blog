# Блок логирования
log_settings = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug_format': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'warning_format': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
        'error_format': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'general_format': {
            'format': '{asctime} {levelname} {message} {module}',
            'style': '{',
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'debug_format',
            'filters': ['require_debug_true'],
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'warning_format',
            'filters': ['require_debug_true'],
        },
        'console_error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'error_format',
            'filters': ['require_debug_true'],
        },
        'console_critical': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'error_format',
            'filters': ['require_debug_true'],
        },
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general_format',
            'filters': ['require_debug_false'],
        },
        'errors': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'general_format',
            'filters': ['require_debug_false'],

        },
        'security': {
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general_format',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'general_format',
            'include_html': True,
        }

    },

    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'console_critical', ],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['errors', 'mail_admins'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['errors', 'mail_admins'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.template': {
            'handlers': ['errors'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.db_backends': {
            'handlers': ['errors'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.security': {
            'handlers': ['security', ],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
