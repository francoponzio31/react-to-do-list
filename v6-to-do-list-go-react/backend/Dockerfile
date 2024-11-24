# Build stage
FROM golang:1.23.2-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o main .

# Run stage
FROM alpine:latest

WORKDIR /app

# The binary is copied from the build stage
COPY --from=builder /app/main .

EXPOSE 8080

CMD ["./main"]
