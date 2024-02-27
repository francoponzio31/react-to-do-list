import { createContext, useEffect, useState } from 'react';
import { getTasks } from "../services/tasks.js"


export const TasksContext = createContext(null);

export function TasksProvider({ children }) {
    
    const [tasks, setTasks] = useState([])

    useEffect(() => {
      async function getTasksAndSet(){
        const tasks = await getTasks()
        setTasks(tasks)
      }
      getTasksAndSet()
    }, [])

    return (
      <TasksContext.Provider value={[tasks, setTasks]}>
        {children}
      </TasksContext.Provider>
    )
  }