import environs

env = environs.Env()
env.read_env("./.env")

api_id = env.int("21662019")
api_hash = env.str("8185723391:AAEfWgN4fmdpqGuVIvhlg6xuiKUrx0kJkcc")

db_type = env.str("DATABASE_TYPE")
db_url = env.str("DATABASE_URL", "")
db_name = env.str("DATABASE_NAME")

test_server = env.bool("TEST_SERVER", False)
modules_repo_branch = env.str("MODULES_REPO_BRANCH", "master")
