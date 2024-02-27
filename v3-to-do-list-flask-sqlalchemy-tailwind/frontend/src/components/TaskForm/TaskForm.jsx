import { useState, useRef, useContext } from "react"
import { getTasks, createTask } from "../../services/tasks.js"
import { TasksContext } from "../../contexts/TasksContext.jsx"


export default function TaskForm(){

    const [_, setTasks] = useContext(TasksContext)
    const [taskText, setTaskText] = useState("")
    const inputRef = useRef(null)

    function handleInputChange(){
        setTaskText(inputRef.current.value)
    }

    async function handleCreate(){
        await createTask({text: taskText})
        const updatedTasks = await getTasks()
        setTasks(updatedTasks)
        setTaskText("")
    }

    return (
        <div className="flex flex-col gap-2">
            <label htmlFor="taskTextInput" className="text-2xl">New task</label>
            <input id="taskTextInput" className="bg-transparent border px-2 py-0.5 rounded" value={taskText} onChange={handleInputChange} ref={inputRef}/>
            <button className="bg-gray-700 rounded py-0.5" onClick={handleCreate}>Create</button>
        </div>
    )
}