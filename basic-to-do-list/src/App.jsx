import { useState } from "react"
import TaskForm from "./components/TaskForm/TaskForm.jsx"
import TasksContainer from "./components/TasksContainer/TasksContainer.jsx"

function App() {

  const [tasks, setTasks] = useState([])

  function handleCreation(newTaskObj){

    const updatedTasks = [
      ...tasks,
      {
        id: tasks.length,
        ...newTaskObj
      }
    ]
    setTasks(updatedTasks)
  }


  return (
    <>
      <TaskForm onCreate={handleCreation}/>
      <TasksContainer tasks={tasks}/>
    </>
  )
}

export default App
