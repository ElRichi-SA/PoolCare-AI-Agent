from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    OCI_CONFIG_FILE: str = "~/.oci/config"

    OCI_PROFILE: str = "DEFAULT"

    OCI_COMPARTMENT_ID: str = ""

    OCI_MODEL_ID: str = ""

    class Config:
        env_file = ".env"


settings = Settings()