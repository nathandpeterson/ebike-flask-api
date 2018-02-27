export AUTOENV_HANDLE_LEAVE=1
source ../venv/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://nathan:bikes@localhost/ebike_dev"