import "./TasksContainer.css"
import TaskCard from "../TaskCard/TaskCard.jsx"


export default function TasksContainer({tasks}){
    return (
        <div className="tasksContainer">
            <span>Tasks:</span>
            {
                tasks.map((task) => (
                    <TaskCard key={task.id} text={task.text}/>
                ))
            }
        </div>
    )
}