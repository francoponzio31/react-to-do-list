package app

import (
	"to_do_list/app/routes"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func CreateApp() *gin.Engine {
	router := gin.Default()

	router.Use(cors.Default())

	routes.RegisterRoutes(router)

	return router
}
