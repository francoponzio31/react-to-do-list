package schemas

type TaskSchema struct {
	ID   int    `json:"id"`
	Text string `json:"text"`
	Done bool   `json:"done"`
}

type UpdateTaskSchema struct {
	Text *string `json:"text,omitempty"`
	Done *bool   `json:"done,omitempty"`
}
