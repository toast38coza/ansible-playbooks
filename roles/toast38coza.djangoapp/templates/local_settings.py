DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{{djangoapp_db_engine}}', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': {{djangoapp_db_name}},                      # Or path to database file if using sqlite3.
        # 'NAME': os.path.join(PROJECT_ROOT, 'data.db'),                      # Or path to database file if using sqlite3.
        'USER': '{{djangoapp_db_user}}',                      # Not used with sqlite3.
        'PASSWORD': '{{djangoapp_db_pass}}',                  # Not used with sqlite3.
        'HOST': '{{djangoapp_db_host}}',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}