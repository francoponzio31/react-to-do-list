import { useState, useContext, useRef } from "react"
import "./TaskForm.css"
import { TasksDispatchContext } from "../../contexts/TasksContext.jsx"


export default function TaskForm(){

    const [taskText, setTaskText] = useState("")
    const tasksDispatch = useContext(TasksDispatchContext)
    const inputRef = useRef(null)

    function handleInputChange(){
        setTaskText(inputRef.current.value)
    }

    function handleCreate(){
        tasksDispatch({
            type: "added",
            taskText: taskText,
        })
        setTaskText("")
    }

    return (
        <div className="taskForm">
            <label htmlFor="taskTextInput">New task</label>
            <input id="taskTextInput" value={taskText} onChange={handleInputChange} ref={inputRef}/>
            <button onClick={handleCreate}>Create</button>
        </div>
    )
}