package repository

import (
	"errors"
	"sync"
	"to_do_list/app/schemas"
)

var (
	tasksDB   = make(map[int]schemas.TaskSchema) // Almacenamiento en memoria
	nextID    = 1                                // ID autoincremental
	tasksLock = sync.Mutex{}                     // Mutex para concurrencia
)

func GetTasks() ([]schemas.TaskSchema, error) {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	tasks := make([]schemas.TaskSchema, 0, len(tasksDB))
	for _, task := range tasksDB {
		tasks = append(tasks, task)
	}

	return tasks, nil
}

func GetTaskById(taskId int) (schemas.TaskSchema, error) {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	task, exists := tasksDB[taskId]
	if !exists {
		return schemas.TaskSchema{}, errors.New("task not found")
	}

	return task, nil
}

func CreateTask(taskData schemas.TaskSchema) (schemas.TaskSchema, error) {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	taskData.ID = nextID
	tasksDB[nextID] = taskData
	nextID++

	return taskData, nil
}

func UpdateTaskById(taskId int, newTaskData schemas.UpdateTaskSchema) (schemas.TaskSchema, error) {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	task, exists := tasksDB[taskId]
	if !exists {
		return schemas.TaskSchema{}, errors.New("task not found")
	}

	// Actualizar solo los campos que no sean nil
	if newTaskData.Text != nil {
		task.Text = *newTaskData.Text // Asignación de puntero a puntero
	}
	if newTaskData.Done != nil {
		task.Done = *newTaskData.Done // Asignación de puntero a puntero
	}

	tasksDB[taskId] = task
	return task, nil
}

func DeleteTaskById(taskId int) error {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	_, exists := tasksDB[taskId]
	if !exists {
		return errors.New("task not found")
	}

	delete(tasksDB, taskId)
	return nil
}
