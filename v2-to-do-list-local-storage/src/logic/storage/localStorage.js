export function getTasksFromLS(){
    const tasksFromLS = window.localStorage.getItem("tasks")
    const tasks = tasksFromLS ? JSON.parse(tasksFromLS) : []
    return tasks
}

export function saveTasksInLS(tasks){
    window.localStorage.setItem("tasks", JSON.stringify(tasks))
}
