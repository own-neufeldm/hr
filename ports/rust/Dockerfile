FROM rust:1.80 AS build
WORKDIR /usr/src/hr4rs
COPY . .
RUN cargo build --release

FROM gcr.io/distroless/cc-debian12 AS run
WORKDIR /usr/bin/hr4rs
COPY --from=build /usr/src/hr4rs/target/release/hr4rs .
ENTRYPOINT ["./hr4rs"]
