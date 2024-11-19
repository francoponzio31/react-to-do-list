package config

import (
	"log"
	"sync"

	"github.com/joho/godotenv"
)

type Config struct {
	AppHost string
	AppPort string
}

var config *Config
var once sync.Once

func GetConfig() *Config {
	once.Do(func() {
		if err := godotenv.Load(); err != nil {
			log.Println("Failed to load .env file")
		}

		config = &Config{
			AppHost: getEnv("HOST", "0.0.0.0"),
			AppPort: getEnv("PORT", "8080"),
		}
	})

	return config
}
