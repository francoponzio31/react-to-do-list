package routes

import (
	"to_do_list/app/controllers"

	"github.com/gin-gonic/gin"
)

func RegisterRoutes(router *gin.Engine) {
	tasksGroup := router.Group("/api/tasks")
	{
		tasksGroup.GET("/", controllers.GetTasks)
		tasksGroup.POST("/", controllers.CreateTask)
		tasksGroup.GET("/:id/", controllers.GetTaskById)
		tasksGroup.PATCH("/:id/", controllers.UpdateTaskById)
		tasksGroup.DELETE("/:id/", controllers.DeleteTaskById)
	}
}
