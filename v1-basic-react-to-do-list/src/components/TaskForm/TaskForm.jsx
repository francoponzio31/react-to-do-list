import { useState } from "react"


export default function TaskForm({onCreate}){

    const [taskText, setTaskText] = useState("")

    function handleInputChange(){
        setTaskText(event.target.value)
    }

    function handleClick(){
        onCreate({
            text: taskText
        })
        setTaskText("")
    }

    return (
        <div className="taskForm">
            <label htmlFor="taskTextInput">Task form</label>
            <input id="taskTextInput" value={taskText} onChange={handleInputChange} />
            <button onClick={handleClick}>Create</button>
        </div>
    )
}