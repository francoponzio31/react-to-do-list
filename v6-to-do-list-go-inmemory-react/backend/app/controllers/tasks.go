package controllers

import (
	"fmt"
	"log"
	"net/http"
	"to_do_list/app/services"
	"to_do_list/app/utils"

	"to_do_list/app/schemas"

	"github.com/gin-gonic/gin"
)

func GetTasks(c *gin.Context) {
	tasks, err := services.GetTasks()
	if err != nil {
		log.Printf("Error getting tasks: %v", err)
		utils.GetErrorResponse(c, http.StatusNotFound, "Error getting tasks")
		return
	}

	utils.GetResponse(
		c,
		http.StatusOK,
		http.StatusText(http.StatusOK),
		gin.H{
			"tasks": tasks,
		},
	)
}

func GetTaskById(c *gin.Context) {
	taskId, err := getIdParam(c)
	if err != nil {
		utils.GetErrorResponse(c, http.StatusBadRequest, "Invalid task ID")
	}

	task, err := services.GetTaskById(taskId)
	if err != nil {
		log.Printf("Error getting task with id %d: %v", taskId, err)
		utils.GetErrorResponse(c, http.StatusNotFound, err.Error())
		return
	}

	utils.GetResponse(
		c,
		http.StatusOK,
		http.StatusText(http.StatusOK),
		gin.H{
			"task": task,
		},
	)

}

func CreateTask(c *gin.Context) {

	var taskData schemas.TaskSchema
	if err := c.ShouldBindJSON(&taskData); err != nil {
		log.Printf("Error deserializing task data: %v", err)
		utils.GetErrorResponse(c,
			http.StatusBadRequest,
			err.Error(),
		)
	}

	newTask, err := services.CreateTask(taskData)
	if err != nil {
		log.Printf("Error creating task: %v", err)
		utils.GetErrorResponse(c, http.StatusBadRequest, fmt.Sprintf("Error creating task"))
		return
	}

	utils.GetResponse(
		c,
		http.StatusOK,
		http.StatusText(http.StatusOK),
		gin.H{
			"task": newTask,
		},
	)
}

func UpdateTaskById(c *gin.Context) {

	taskId, err := getIdParam(c)
	if err != nil {
		utils.GetErrorResponse(c, http.StatusBadRequest, "Invalid task ID")
	}

	var taskData schemas.UpdateTaskSchema
	if err := c.ShouldBindJSON(&taskData); err != nil {
		log.Printf("Error deserializing task data: %v", err)
		utils.GetErrorResponse(c,
			http.StatusBadRequest,
			err.Error(),
		)
	}

	task, err := services.UpdateTaskById(taskId, taskData)
	if err != nil {
		log.Printf("Error updating task with id %d: %v", taskId, err)
		utils.GetErrorResponse(c, http.StatusNotFound, fmt.Sprintf("Error updating task %d", taskId))
		return
	}

	utils.GetResponse(
		c,
		http.StatusOK,
		http.StatusText(http.StatusOK),
		gin.H{
			"task": task,
		},
	)
}

func DeleteTaskById(c *gin.Context) {
	taskId, err := getIdParam(c)
	if err != nil {
		utils.GetErrorResponse(c, http.StatusBadRequest, "Invalid task ID")
	}

	err = services.DeleteTaskById(taskId)
	if err != nil {
		log.Printf("Error deleting task with id %d: %v", taskId, err)
		utils.GetErrorResponse(c, http.StatusNotFound, fmt.Sprintf("Error deleting task %d", taskId))
		return
	}

	c.Status(http.StatusNoContent)
}
