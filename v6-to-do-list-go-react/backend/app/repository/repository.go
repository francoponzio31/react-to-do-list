package repository

import (
	"database/sql"
	"fmt"
	"log"
	"to_do_list/app/repository/memory"
	"to_do_list/app/repository/pg"
	"to_do_list/app/schemas"

	configPkg "to_do_list/app/config"

	_ "github.com/lib/pq"
)

type TaskRepository interface {
	GetTasks() ([]schemas.TaskSchema, error)
	GetTaskById(taskId int) (schemas.TaskSchema, error)
	CreateTask(taskData schemas.TaskSchema) (schemas.TaskSchema, error)
	UpdateTaskById(taskId int, newTaskData schemas.UpdateTaskSchema) (schemas.TaskSchema, error)
	DeleteTaskById(taskId int) error
	DeleteTasksByIds(taskIds []int) error
}

var taskRepo TaskRepository

func InitTaskRepository() {
	config := configPkg.GetConfig()

	switch config.Persistence {
	case "pg":
		connStr := fmt.Sprintf(
			"host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
			config.DBHost, config.DBPort, config.DBPass, config.DBPass, config.DBName,
		)
		db, err := sql.Open("postgres", connStr)
		if err != nil {
			log.Fatal(err)
		}
		taskRepo = pg.NewPgTaskRepository(db)
	default:
		taskRepo = &memory.MemoryTaskRepository{}
	}
}

func GetTasks() ([]schemas.TaskSchema, error) {
	return taskRepo.GetTasks()
}

func GetTaskById(taskId int) (schemas.TaskSchema, error) {
	return taskRepo.GetTaskById(taskId)
}

func CreateTask(taskData schemas.TaskSchema) (schemas.TaskSchema, error) {
	return taskRepo.CreateTask(taskData)
}

func UpdateTaskById(taskId int, newTaskData schemas.UpdateTaskSchema) (schemas.TaskSchema, error) {
	return taskRepo.UpdateTaskById(taskId, newTaskData)
}

func DeleteTaskById(taskId int) error {
	return taskRepo.DeleteTaskById(taskId)
}

func DeleteTasksByIds(taskIds []int) error {
	return taskRepo.DeleteTasksByIds(taskIds)
}
