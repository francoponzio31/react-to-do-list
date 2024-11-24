package config

import (
	"log"
	"sync"

	"github.com/joho/godotenv"
)

type Config struct {
	AppHost     string
	AppPort     string
	Persistence string
	DBName      string
	DBUser      string
	DBPass      string
	DBHost      string
	DBPort      string
}

var config *Config
var once sync.Once

func GetConfig() *Config {
	once.Do(func() {
		if err := godotenv.Load(); err != nil {
			log.Println("Failed to load .env file")
		}

		config = &Config{
			AppHost:     getEnv("HOST", "not_set"),
			AppPort:     getEnv("PORT", "not_set"),
			Persistence: getEnv("PERSISTENCE", "not_set"),
			DBName:      getEnv("DB_NAME", "not_set"),
			DBUser:      getEnv("DB_USER", "not_set"),
			DBPass:      getEnv("DB_PASSWORD", "not_set"),
			DBHost:      getEnv("DB_HOST", "not_set"),
			DBPort:      getEnv("DB_PORT", "not_set"),
		}
	})

	return config
}
