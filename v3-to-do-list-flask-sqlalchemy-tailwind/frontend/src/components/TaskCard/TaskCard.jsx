import { useContext, useState, useRef } from "react"
import { TasksContext } from "../../contexts/TasksContext.jsx"
import { getTasks, deleteTaskById, updateTaskById } from "../../services/tasks.js"


function TaskBtn({text, handleClick}){
    return (
        <button onClick={handleClick} className="bg-gray-700 px-2 py-0.5 rounded text-sm ">{text}</button>
    )
}

function TaskStatusBudget({done}){
    return (
        <span className={`absolute top-0 right-0 rounded px-1.5 m-2 text-sm ${done ? "bg-green-600" : "bg-red-600"}`}>
            {done ? "Done" : "To do"}
        </span>
    )
}

export default function TaskCard({id, text, done}){

    const [_, setTasks] = useContext(TasksContext)
    const [editing, setEditing] = useState(false)
    const [inputText, setInputText] = useState(text)
    const inputTextRef = useRef(null)

    async function handleDelete(){
        await deleteTaskById(id)
        const updatedTasks = await getTasks()
        setTasks(updatedTasks)
    }

    async function handleUpdateStatus(){
        const data = await updateTaskById(id, {done: !done})
        const updatedTasks = await getTasks()
        setTasks(updatedTasks)
    }

    function handleInputChange(){
        setInputText(inputTextRef.current.value)
    }

    function handleEdit(){
        setEditing(true)
        inputTextRef.current.removeAttribute("readOnly")
        inputTextRef.current.focus()
    }

    async function handleSave(){
        await updateTaskById(id, {text: inputText})
        const updatedTasks = await getTasks()
        setTasks(updatedTasks)
        setEditing(false)
        inputTextRef.current.setAttribute("readOnly", true)
    }

    return (
        <div className="relative bg-[#070d16] rounded px-7 py-4">
            <TaskStatusBudget done={done}/>
            <input 
                value={inputText} 
                className="bg-transparent text-xl outline-none" 
                readOnly={true} 
                ref={inputTextRef} 
                onChange={handleInputChange}
            />
            <div className="mt-3 flex gap-2">
                <TaskBtn handleClick={handleDelete} text={"Delete"}/>
                <TaskBtn handleClick={handleUpdateStatus} text={"Update status"}/>
                {!editing && <TaskBtn handleClick={handleEdit} text={"Edit"}/>}
                {editing && <TaskBtn handleClick={handleSave} text={"Save"}/>}
            </div>
        </div>
    )
}