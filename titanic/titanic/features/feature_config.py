"""List the features in a config dictionary."""

from .features.features import age_bin

CONFIG = {
    'features': [
        {
            'name': 'pclass',
            'type': 'categoric',
        },
        {
            'name': 'sex',
            'type': 'categoric',
        },
        {
            'name': 'age',
            'type': 'numeric',
        },
        {
            'name': 'fare',
            'type': 'numeric',
        },
        {
            'name': 'age_bin',
            'type': 'categoric',
            'function': age_bin
        },
        {
            'name': 'embarked',
            'type': 'categoric',
        },
    ],
    'target': {'name': 'survived'}
}
