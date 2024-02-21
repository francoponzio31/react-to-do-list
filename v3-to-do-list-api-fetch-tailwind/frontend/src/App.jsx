import TaskForm from "./components/TaskForm/TaskForm.jsx"
import TasksContainer from "./components/TasksContainer/TasksContainer.jsx"
import { TasksProvider } from "./contexts/TasksContext.jsx"


function App() {

  return (
    <main className="bg-gray-900 text-white font-sans min-h-screen flex flex-col place-items-center font-medium">
      <TasksProvider>
        <section className="w-1/2 flex flex-col gap-12 mt-10">
          <TaskForm/>
          <TasksContainer/>
        </section>
      </TasksProvider>
    </main>
  )
}

export default App
