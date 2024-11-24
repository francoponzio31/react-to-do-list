package app

import (
	"to_do_list/app/routes"

	repositoryPkg "to_do_list/app/repository"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func CreateApp() *gin.Engine {
	router := gin.Default()

	router.Use(cors.Default())

	repositoryPkg.InitTaskRepository()

	routes.RegisterRoutes(router)

	return router
}
