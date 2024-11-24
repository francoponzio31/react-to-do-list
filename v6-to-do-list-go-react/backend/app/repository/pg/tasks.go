package pg

import (
	"database/sql"
	"errors"
	"to_do_list/app/schemas"
)

type PgTaskRepository struct {
	db *sql.DB
}

func NewPgTaskRepository(db *sql.DB) *PgTaskRepository {
	return &PgTaskRepository{db: db}
}

func (r *PgTaskRepository) GetTasks() ([]schemas.TaskSchema, error) {
	rows, err := r.db.Query("SELECT id, text, done FROM tasks ORDER BY id")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var tasks []schemas.TaskSchema
	for rows.Next() {
		var task schemas.TaskSchema
		if err := rows.Scan(&task.ID, &task.Text, &task.Done); err != nil {
			return nil, err
		}
		tasks = append(tasks, task)
	}
	if len(tasks) == 0 {
		return []schemas.TaskSchema{}, nil
	}
	return tasks, nil
}

func (r *PgTaskRepository) GetTaskById(taskId int) (schemas.TaskSchema, error) {
	var task schemas.TaskSchema
	err := r.db.QueryRow("SELECT id, text, done FROM tasks WHERE id = $1", taskId).Scan(&task.ID, &task.Text, &task.Done)
	if err == sql.ErrNoRows {
		return schemas.TaskSchema{}, errors.New("task not found")
	} else if err != nil {
		return schemas.TaskSchema{}, err
	}
	return task, nil
}

func (r *PgTaskRepository) CreateTask(taskData schemas.TaskSchema) (schemas.TaskSchema, error) {
	err := r.db.QueryRow("INSERT INTO tasks (text, done) VALUES ($1, $2) RETURNING id", taskData.Text, taskData.Done).Scan(&taskData.ID)
	if err != nil {
		return schemas.TaskSchema{}, err
	}
	return taskData, nil
}

func (r *PgTaskRepository) UpdateTaskById(taskId int, newTaskData schemas.UpdateTaskSchema) (schemas.TaskSchema, error) {
	var task schemas.TaskSchema
	err := r.db.QueryRow("SELECT id, text, done FROM tasks WHERE id = $1", taskId).Scan(&task.ID, &task.Text, &task.Done)
	if err == sql.ErrNoRows {
		return schemas.TaskSchema{}, errors.New("task not found")
	} else if err != nil {
		return schemas.TaskSchema{}, err
	}

	if newTaskData.Text != nil {
		task.Text = *newTaskData.Text
	}
	if newTaskData.Done != nil {
		task.Done = *newTaskData.Done
	}

	_, err = r.db.Exec("UPDATE tasks SET text = $1, done = $2 WHERE id = $3", task.Text, task.Done, task.ID)
	if err != nil {
		return schemas.TaskSchema{}, err
	}
	return task, nil
}

func (r *PgTaskRepository) DeleteTaskById(taskId int) error {
	result, err := r.db.Exec("DELETE FROM tasks WHERE id = $1", taskId)
	if err != nil {
		return err
	}
	rowsAffected, err := result.RowsAffected()
	if err != nil {
		return err
	}
	if rowsAffected == 0 {
		return errors.New("task not found")
	}
	return nil
}

func (r *PgTaskRepository) DeleteTasksByIds(taskIds []int) error {
	tx, err := r.db.Begin()
	if err != nil {
		return err
	}

	for _, taskId := range taskIds {
		result, err := tx.Exec("DELETE FROM tasks WHERE id = $1", taskId)
		if err != nil {
			tx.Rollback()
			return err
		}
		rowsAffected, err := result.RowsAffected()
		if err != nil {
			tx.Rollback()
			return err
		}
		if rowsAffected == 0 {
			tx.Rollback()
			return errors.New("one or more tasks not found")
		}
	}

	err = tx.Commit()
	if err != nil {
		return err
	}
	return nil
}
