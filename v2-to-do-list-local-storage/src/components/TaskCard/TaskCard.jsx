import "./TaskCard.css"
import { useContext, useState, useRef } from "react"
import { TasksDispatchContext } from "../../contexts/TasksContext.jsx"


function TaskBtn({text, handleClick}){
    return (
        <button onClick={handleClick} className="taskBtn">{text}</button>
    )
}

function TaskStatusBudget({done}){
    return (
        <span className={`taskStatusBudget ${done ? "done" : "todo"}`}>
            {done ? "Done" : "To do"}
        </span>
    )
}

export default function TaskCard({id, text, done}){
    const dispatch = useContext(TasksDispatchContext)
    const [editing, setEditing] = useState(false)
    const [inputText, setInputText] = useState(text)
    const inputTextRef = useRef(null)

    function handleDelete(){
        dispatch({
            type: "deleted",
            taskId: id
        })
    }

    function handleUpdateStatus(){
        dispatch({
            type: "statusUpdated",
            taskId: id
        })
    }

    function handleInputChange(){
        setInputText(inputTextRef.current.value)
    }

    function handleEdit(){
        setEditing(true)
        inputTextRef.current.removeAttribute("readOnly")
        inputTextRef.current.focus()
    }

    function handleSave(){
        dispatch({
            type: "edited",
            taskId: id,
            newText: inputText
        })
        setEditing(false)
        inputTextRef.current.setAttribute("readOnly", true)
    }

    return (
        <div className="taskCard">
            <TaskStatusBudget done={done}/>
            <input 
                value={inputText} 
                className="taskText" 
                readOnly={true} 
                ref={inputTextRef} 
                onChange={handleInputChange}
            />
            <div className="taskBtnContainer">
                <TaskBtn handleClick={handleDelete} text={"Delete"}/>
                <TaskBtn handleClick={handleUpdateStatus} text={"Update status"}/>
                {!editing && <TaskBtn handleClick={handleEdit} text={"Edit"}/>}
                {editing && <TaskBtn handleClick={handleSave} text={"Save"}/>}
            </div>
        </div>
    )
}