package memory

import (
	"errors"
	"sync"
	"to_do_list/app/schemas"
)

var (
	tasksDB   = make(map[int]schemas.TaskSchema)
	nextID    = 1
	tasksLock = sync.Mutex{}
)

type MemoryTaskRepository struct{}

func (r *MemoryTaskRepository) GetTasks() ([]schemas.TaskSchema, error) {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	tasks := make([]schemas.TaskSchema, 0, len(tasksDB))
	for _, task := range tasksDB {
		tasks = append(tasks, task)
	}
	return tasks, nil
}

func (r *MemoryTaskRepository) GetTaskById(taskId int) (schemas.TaskSchema, error) {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	task, exists := tasksDB[taskId]
	if !exists {
		return schemas.TaskSchema{}, errors.New("task not found")
	}
	return task, nil
}

func (r *MemoryTaskRepository) CreateTask(taskData schemas.TaskSchema) (schemas.TaskSchema, error) {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	taskData.ID = nextID
	nextID++
	tasksDB[taskData.ID] = taskData
	return taskData, nil
}

func (r *MemoryTaskRepository) UpdateTaskById(taskId int, newTaskData schemas.UpdateTaskSchema) (schemas.TaskSchema, error) {
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

func (r *MemoryTaskRepository) DeleteTaskById(taskId int) error {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	_, exists := tasksDB[taskId]
	if !exists {
		return errors.New("task not found")
	}

	delete(tasksDB, taskId)
	return nil
}

func (r *MemoryTaskRepository) DeleteTasksByIds(taskIds []int) error {
	tasksLock.Lock()
	defer tasksLock.Unlock()

	for _, taskId := range taskIds {
		if _, exists := tasksDB[taskId]; !exists {
			return errors.New("one or more tasks not found")
		}
	}

	for _, taskId := range taskIds {
		delete(tasksDB, taskId)
	}

	return nil
}
