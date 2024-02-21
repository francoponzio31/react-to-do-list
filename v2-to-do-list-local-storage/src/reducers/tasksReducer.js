export default function tasksReducer(tasks, action){
    switch (action.type){
        case "added": {
            return [
                ...tasks,
                {
                  id: tasks.length ? tasks[tasks.length-1].id+1 : 0,
                  text: action.taskText,
                  done: false
                }
              ]
        }
        case "statusUpdated": {
            return tasks.map((task) => {
              if (task.id === action.taskId){
                return {
                  ...task,
                  done: !task.done
                }
              }
              else {
                return task
              }
            })
        }
        case "deleted": {
            return tasks.filter(task => task.id !== action.taskId)
        }
        case "edited": {
          return tasks.map((task) => {
            if (task.id === action.taskId){
              return {
                ...task,
                text: action.newText
              }
            }
            else {
              return task
            }
          })
        }
        default: {
          throw Error('Unknown action: ' + action.type);
        }
    }
}
