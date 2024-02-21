import { createContext, useEffect, useReducer } from 'react';
import tasksReducer from "../reducers/tasksReducer.js"
import { saveTasksInLS, getTasksFromLS } from "../logic/storage/localStorage.js"


export const TasksContext = createContext(null);
export const TasksDispatchContext = createContext(null);

export function TasksProvider({ children }) {
    
    const initialTasks = getTasksFromLS()
    const [tasks, dispatch] = useReducer(tasksReducer, initialTasks)
  
    useEffect(() => {
      saveTasksInLS(tasks)
    }, [tasks])
  
    return (
      <TasksContext.Provider value={tasks}>
        <TasksDispatchContext.Provider value={dispatch}>
          {children}
        </TasksDispatchContext.Provider>
      </TasksContext.Provider>
    )
  }