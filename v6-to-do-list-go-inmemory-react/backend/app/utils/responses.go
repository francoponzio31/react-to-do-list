package utils

import (
	"time"

	"github.com/gin-gonic/gin"
)

func GetResponse(c *gin.Context, code int, message string, extraFields gin.H) {
	response := gin.H{
		"message": message,
	}

	for key, value := range extraFields {
		response[key] = value
	}

	c.JSON(code, response)
}

func GetErrorResponse(c *gin.Context, code int, message string) {
	c.JSON(code, gin.H{
		"message":   message,
		"timestamp": time.Now().Format(time.RFC3339),
	})
}
