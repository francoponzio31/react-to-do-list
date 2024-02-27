const API_BASE_URL = "http://localhost:8000"


export async function getTasks(){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/`)
        const tasks = await response.json()

        return true, tasks
    } catch (error) {
        console.log(error)
        return false, "request error"
    }
}

export async function getTaskById(taskId){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/${taskId}/`)
        const task = await response.json()
        return true, task
    } catch (error) {
        console.log(error)
        return false, "request error"
    }
}

export async function createTask(taskObj){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/`,{
            method: "POST",
            body: JSON.stringify(taskObj),
            headers: {
              "Content-Type": "application/json",
            },
        })
        const data = await response.json()
        return true, data
    } catch (error) {
        console.log(error)
        return false, "request error"
    }
}

export async function updateTaskById(taskId, taskObj){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/${taskId}/`,{
            method: "PATCH",
            body: JSON.stringify(taskObj),
            headers: {
              "Content-Type": "application/json",
            },
        })
        const data = await response.json()
        return true, data
    } catch (error) {
        console.log(error)
        return false, "request error"
    }
}

export async function deleteTaskById(taskId){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/${taskId}/`,{
            method: "DELETE"
        })
        const data = await response.json()
        return true, data
    } catch (error) {
        console.log(error)
        return false, "request error"
    }
}