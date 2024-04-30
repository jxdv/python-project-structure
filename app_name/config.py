from pathlib import Path

from dotenv import dotenv_values

root_dir = Path(__file__).parent.parent
env_shared = root_dir / ".env"
env_dev = root_dir / ".env.dev"

config = {
	**dotenv_values(env_shared),
	**dotenv_values(env_dev)
}
