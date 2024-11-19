package controllers

import (
	"log"
	"strconv"

	"github.com/gin-gonic/gin"
)

func getIdParam(c *gin.Context) (int, error) {
	idParam := c.Param("id")

	id, err := strconv.Atoi(idParam)
	if err != nil {
		log.Printf("Error parsing task id: %v", err)
		return 0, err
	}

	return id, nil
}
