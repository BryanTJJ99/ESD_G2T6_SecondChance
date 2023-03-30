# FROM openjdk:19
# WORKDIR /usr/src/app
# COPY ./target/department-0.0.1-SNAPSHOT.jar department-0.0.1-SNAPSHOT.jar
# EXPOSE 8080
# CMD ["java", "-jar", "./department-0.0.1-SNAPSHOT.jar"]

FROM maven:3.8.1-openjdk-17-slim AS builder
WORKDIR ./
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn clean -DskipTests -e -B package

FROM eclipse-temurin:17-jdk-alpine
VOLUME /tmp
COPY --from=builder /target/*.jar /app.jar
ENTRYPOINT ["java","-jar","/app.jar"]