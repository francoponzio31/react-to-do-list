package config

import (
	"log"
	"os"
	"strconv"
)

func getEnv(key string, defaultValue string) string {
	if value, exists := os.LookupEnv(key); exists {
		return value
	}
	return defaultValue
}

func getEnvAsInt(key string, defaultValue int) int {
	valueStr := getEnv(key, strconv.Itoa(defaultValue))
	value, err := strconv.Atoi(valueStr)
	if err != nil {
		log.Printf("Warning: Failed to parse %s as integer. Using default value %d\n", key, defaultValue)
		return defaultValue
	}
	return value
}
