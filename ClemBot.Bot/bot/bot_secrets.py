import json
import os
from typing import Any, get_origin, get_args

from bot.errors import ConfigAccessError
from bot.utils.logging_utils import get_logger

log = get_logger(__name__)


class BotSecrets:
    def __init__(self) -> None:
        self._client_token: str | None = None
        self._client_secret: str | None = None
        self._bot_token: str | None = None
        self._bot_prefix: str | None = None
        self._repl_url: str | None = None
        self._github_url: str | None = None
        self._api_url: str | None = None
        self._api_key: str | None = None
        self._bot_only: bool | None = None
        self._startup_log_channel_ids: list[int] | None = None
        self._error_log_channel_ids: list[int] | None = None
        self._site_url: str | None = None
        self._docs_url: str | None = None
        self._allow_bot_input_ids: list[int] | None = None

    @property
    def client_token(self) -> str:
        if not self._client_token:
            raise ConfigAccessError("client_token has not been initialized")
        return self._client_token

    @client_token.setter
    def client_token(self, value: str | None) -> None:
        if self._client_token:
            raise ConfigAccessError("client_token has already been initialized")
        self._client_token = value

    @property
    def client_secret(self) -> str:
        if not self._client_secret:
            raise ConfigAccessError("client_secret has not been initialized")
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value: str | None) -> None:
        if self._client_secret:
            raise ConfigAccessError("client_secret has already been initialized")
        self._client_secret = value

    @property
    def bot_token(self) -> str:
        if not self._bot_token:
            raise ConfigAccessError("bot_token has not been initialized")
        return self._bot_token

    @bot_token.setter
    def bot_token(self, value: str | None) -> None:
        if self._bot_token:
            raise ConfigAccessError("bot_token has already been initialized")
        self._bot_token = value

    @property
    def bot_only(self) -> bool:
        if not self._bot_only:
            return False
        return self._bot_only

    @bot_only.setter
    def bot_only(self, value: bool) -> None:
        if self.bot_only:
            raise ConfigAccessError("bot_only has already been initialized")

        if isinstance(value, str):
            self._bot_only = bool(value)
        else:
            self._bot_only = value

    @property
    def bot_prefix(self) -> str:
        if not self._bot_prefix:
            return "!"
        return self._bot_prefix

    @bot_prefix.setter
    def bot_prefix(self, value: str | None) -> None:
        if self._bot_prefix:
            raise ConfigAccessError("bot_prefix has already been initialized")
        self._bot_prefix = value

    @property
    def github_url(self) -> str:
        if not self._github_url:
            return "https://github.com/ClemsonCPSC-Discord/ClemBot"
        return self._github_url

    @github_url.setter
    def github_url(self, value: str | None) -> None:
        if self._github_url:
            raise ConfigAccessError("github_url has already been initialized")
        self._github_url = value

    @property
    def repl_url(self) -> str:
        if not self._repl_url:
            raise ConfigAccessError("repl_url has not been intialized")
        return self._repl_url

    @repl_url.setter
    def repl_url(self, value: str | None) -> None:
        if self._repl_url:
            raise ConfigAccessError("repl_url has already been initialized")
        self._repl_url = value

    @property
    def startup_log_channel_ids(self) -> list[int]:
        if not self._startup_log_channel_ids:
            raise ConfigAccessError("startup_log_channel_ids has not been initialized")
        return self._startup_log_channel_ids

    @startup_log_channel_ids.setter
    def startup_log_channel_ids(self, value: list[int]) -> None:
        if self._startup_log_channel_ids:
            raise ConfigAccessError("startup_log_channel_ids has already been initialized")
        self._startup_log_channel_ids = value

    @property
    def error_log_channel_ids(self) -> list[int]:
        if not self._error_log_channel_ids:
            raise ConfigAccessError("error_log_channel_ids has not been initialized")
        return self._error_log_channel_ids

    @error_log_channel_ids.setter
    def error_log_channel_ids(self, value: list[int]) -> None:
        if self._error_log_channel_ids:
            raise ConfigAccessError("error_log_channel_ids has already been initialized")
        self._error_log_channel_ids = value

    @property
    def api_url(self) -> str:
        if not self._api_url:
            raise ConfigAccessError("api_url has not been initialized")
        return self._api_url

    @api_url.setter
    def api_url(self, value: str | None) -> None:
        if self._api_url:
            raise ConfigAccessError("api_url has already been initialized")
        self._api_url = value

    @property
    def api_key(self) -> str:
        if not self._api_key:
            raise ConfigAccessError("api_key has not been initialized")
        return self._api_key

    @api_key.setter
    def api_key(self, value: str | None) -> None:
        if self._api_key:
            raise ConfigAccessError("api_key has already been initialized")
        self._api_key = value

    @property
    def site_url(self) -> str:
        if not self._site_url:
            raise ConfigAccessError("site_url has not been initialized")
        return self._site_url

    @site_url.setter
    def site_url(self, value: str | None) -> None:
        if self._site_url:
            raise ConfigAccessError("site_url has already been initialized")
        self._site_url = value

    @property
    def docs_url(self) -> str:
        if not self._docs_url:
            raise ConfigAccessError("docs_url has not been initialized")
        return self._docs_url

    @docs_url.setter
    def docs_url(self, value: str | None) -> None:
        if self._docs_url:
            raise ConfigAccessError("docs_url has already been initialized")
        self._docs_url = value

    @property
    def allow_bot_input_ids(self) -> list[int]:
        if self._allow_bot_input_ids is None:
            raise ConfigAccessError("allow_bot_input_ids has not been initialized")
        return self._allow_bot_input_ids

    @allow_bot_input_ids.setter
    def allow_bot_input_ids(self, value: list[int] | None) -> None:
        if self._allow_bot_input_ids:
            raise ConfigAccessError("allow_bot_input_ids has already been initialized")
        self._allow_bot_input_ids = value

    def _convert_value(self, value: str, type_hint: type) -> Any:
        """Convert a string value from environment variable to the appropriate type."""

        def convert_scalar(val: str, target_type: type) -> Any:
            """Convert a single scalar value to the target type."""
            match target_type:
                case t if t is bool:
                    return bool(val)
                case t if t is int:
                    return int(val)
                case _:
                    return val

        origin = get_origin(type_hint)

        if origin is list:
            args = get_args(type_hint)
            inner_type = args[0] if args else str
            items = [item.strip() for item in value.split(",")]
            return [convert_scalar(item, inner_type) for item in items]

        return convert_scalar(value, type_hint)

    def _load_secret(
        self,
        key: str,
        json_data: dict | None,
        type_hint: type = str,
        default: Any = None,
    ) -> Any:
        """
        Load a secret from environment variable first, then fall back to JSON file, then default.

        Args:
            key: The configuration key name
            json_data: Merged JSON configuration data
            type_hint: The expected type (e.g., str, int, bool, list[int])
            default: Default value if not found in env or json
        """
        # Try environment variable first
        env_value = os.environ.get(key)
        if env_value is not None:
            value = self._convert_value(env_value, type_hint)
            log.info(f"{key}: loaded from environment")
            return value

        # Fall back to JSON file
        if json_data is not None and key in json_data:
            value = json_data[key]
            log.info(f"{key}: loaded from json file")
            return value

        # Use default if available
        if default is not None:
            log.info(f"{key}: loaded from default")
            return default

        raise ConfigAccessError(f"No value for configuration: '{key}' found")

    def load_secrets(self, *sources: str) -> None:
        """
        Load secrets with priority: environment variables > rightmost source > ... > leftmost source > defaults.
        Logs the source of each secret at INFO level.

        Args:
            *sources: Paths to JSON configuration files. Files are merged with rightmost having highest priority.
                     If no sources provided, only environment variables and defaults will be used.
        """
        json_data = {}
        for source_path in sources:
            try:
                with open(source_path) as f:
                    file_data = json.loads(f.read())
                    # Merge with rightmost having priority (overwrites existing keys)
                    json_data.update(file_data)
                    log.info(f"Loaded configuration from {source_path}")
            except FileNotFoundError:
                log.info(f"No file found at {source_path}, skipping")
            except json.JSONDecodeError as e:
                log.error(f"Failed to parse JSON from {source_path}: {e}")
                raise

        # Pass merged data (or None if no data loaded) to secret loading
        merged_data = json_data if json_data else None

        # Load each secret
        self.client_token = self._load_secret("CLIENT_TOKEN", merged_data, str)
        self.client_secret = self._load_secret("CLIENT_SECRET", merged_data, str)
        self.bot_token = self._load_secret("BOT_TOKEN", merged_data, str)
        self.bot_prefix = self._load_secret("BOT_PREFIX", merged_data, str, default="!")
        self.bot_only = self._load_secret("BOT_ONLY", merged_data, bool, default=False)  # type: ignore
        self.startup_log_channel_ids = self._load_secret("STARTUP_LOG_CHANNEL_IDS", merged_data, list[int])
        self.error_log_channel_ids = self._load_secret("ERROR_LOG_CHANNEL_IDS", merged_data, list[int])
        self.repl_url = self._load_secret("REPL_URL", merged_data, str)
        self.github_url = self._load_secret(
            "GITHUB_URL", merged_data, str, default="https://github.com/ClemsonCPSC-Discord/ClemBot"
        )
        self.api_url = self._load_secret("API_URL", merged_data, str)
        self.api_key = self._load_secret("API_KEY", merged_data, str)
        self.site_url = self._load_secret("SITE_URL", merged_data, str)
        self.docs_url = self._load_secret("DOCS_URL", merged_data, str)
        self.allow_bot_input_ids = self._load_secret("ALLOW_BOT_INPUT_IDS", merged_data, list[int])

        log.info("All bot secrets loaded successfully")


secrets = BotSecrets()
