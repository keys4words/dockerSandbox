FROM golang:1.16-alpine AS build
WORKDIR /app
COPY go.mod ./
COPY go.sum ./
RUN go mod download
COPY *.go ./
RUN go build -o /server

FROM alpine
WORKDIR /
COPY --from=build /server /server
EXPOSE 8080
ENTRYPOINT ["/server"]