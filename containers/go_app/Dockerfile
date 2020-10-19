FROM golang:1.12.0-alpine3.9

RUN mkdir /app
ADD ./go_app /app
WORKDIR /app
RUN go build -o main .

EXPOSE 8000
CMD ["/app/main"]