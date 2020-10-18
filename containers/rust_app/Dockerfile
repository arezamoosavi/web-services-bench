FROM rust:1.47.0-slim-buster

RUN apt-get update \
    && apt-get install -y ca-certificates tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/rust_app
ADD ./rust_app ./opt/rust_app

WORKDIR /opt/rust_app
RUN cargo build --release

RUN chmod a+rwx ./target/release/rust_app

EXPOSE 8000
CMD ["./target/release/rust_app"]