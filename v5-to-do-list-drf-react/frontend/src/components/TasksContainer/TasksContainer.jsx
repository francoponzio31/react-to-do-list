import TaskCard from "../TaskCard/TaskCard.jsx"
import { useContext } from "react"
import { TasksContext } from "../../contexts/TasksContext.jsx"


export default function TasksContainer(){
    const [tasks, _] = useContext(TasksContext)

    console.log(tasks);
    

    return (
        <div className="flex flex-col gap-3">
            <label className="text-2xl">Tasks:</label>
            
            {tasks.length ? 
                tasks.map((task) => (
                    <TaskCard key={task.id} id={task.id} text={task.text} done={task.done}/>
                ))
                : <span>No tasks yet...</span>
            }
        </div>
    )
}