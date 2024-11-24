const API_BASE_URL = "http://localhost:8000"


export async function getTasks(){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/`)
        const data = await response.json()
        return data.tasks
    } catch (error) {
        console.log(error)
    }
}

export async function getTaskById(taskId){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/${taskId}/`)
        const data = await response.json()
        return data.task
    } catch (error) {
        console.log(error)
        return "request error"
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
        return data
    } catch (error) {
        console.log(error)
        return "request error"
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
        return data
    } catch (error) {
        console.log(error)
        return "request error"
    }
}

export async function deleteTaskById(taskId){
    try {
        const response = await fetch(`${API_BASE_URL}/api/tasks/${taskId}/`,{
            method: "DELETE"
        })
        const data = await response.json()
        return data
    } catch (error) {
        console.log(error)
        return "request error"
    }
}