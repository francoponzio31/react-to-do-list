import "./TasksContainer.css"
import TaskCard from "../TaskCard/TaskCard.jsx"
import { useContext } from "react"
import { TasksContext } from "../../contexts/TasksContext.jsx"


export default function TasksContainer(){
    const tasks = useContext(TasksContext)
    return (
        <div className="tasksContainer">
            <label>Tasks:</label>
            
            {tasks.length ? 
                tasks.map((task) => (
                    <TaskCard key={task.id} id={task.id} text={task.text} done={task.done}/>
                ))
                : <span>No tasks yet...</span>
            }
        </div>
    )
}