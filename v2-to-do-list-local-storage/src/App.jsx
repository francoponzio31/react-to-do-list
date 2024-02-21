import TaskForm from "./components/TaskForm/TaskForm.jsx"
import TasksContainer from "./components/TasksContainer/TasksContainer.jsx"
import { TasksProvider } from "./contexts/TasksContext.jsx"


function App() {
  

  return (
    <>
      <TasksProvider>
        <TaskForm/>
        <TasksContainer/>
      </TasksProvider>
    </>
  )
}

export default App
