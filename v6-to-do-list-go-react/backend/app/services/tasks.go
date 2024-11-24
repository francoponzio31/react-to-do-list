package services

import (
	"to_do_list/app/repository"
	"to_do_list/app/schemas"
)

func GetTasks() ([]schemas.TaskSchema, error) {
	tasks, err := repository.GetTasks()
	if err != nil {
		return nil, err
	}
	return tasks, nil
}

func GetTaskById(taskId int) (schemas.TaskSchema, error) {

	task, err := repository.GetTaskById(taskId)
	if err != nil {
		return schemas.TaskSchema{}, err
	}
	return task, nil
}

func CreateTask(taskData schemas.TaskSchema) (schemas.TaskSchema, error) {
	task, err := repository.CreateTask(taskData)
	if err != nil {
		return schemas.TaskSchema{}, err
	}
	return task, nil
}

func UpdateTaskById(taskId int, taskData schemas.UpdateTaskSchema) (schemas.TaskSchema, error) {
	task, err := repository.UpdateTaskById(taskId, taskData)
	if err != nil {
		return schemas.TaskSchema{}, err
	}
	return task, nil
}

func DeleteTaskById(taskId int) error {
	err := repository.DeleteTaskById(taskId)
	if err != nil {
		return err
	}
	return nil
}
