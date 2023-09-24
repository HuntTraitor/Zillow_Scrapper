A website that scraps the zillow market in seattle daily and stores that information into time graphs displaying the appreciation rate of different zipcodes over time.

To clone this repo and play around with the codebase, you first need to install Docker. We use Docker to ensure everyone has the same development enviroment so minimize system specific bugs and dependency conflicts.

Once you have installed Docker, clone the repository either into a docker container or into any folder on your local machine. If you are on VSCode, you can press f1 and type in 'Dev Containers: Open Folder in Container...' and choose to open it from docker-compose.yml to kickstart the docker container and begin development. If you are not using VSCode, open a terminal and type 'docker-compose up -d' to start the container.

The next thing you MUST do to use most of the backend codebase is to create a .env file in the format of the .env.example file and to put in your database credentials. This is to ensure secure access to the mongoDB database.

This project is developed in flask with the server file being 'app.py' in the root directory. Type 'python3 app.py' to run the development server on your local machine. It is important to run this server with that command specifically and not 'Flask run' because of port forwarding issues. To run the daily script that both updates the databases and the static graphs, run 'python3 src/run.py' NOTE: Because this command will override things inside of the database and has a lot of overhead, try to use this command as minimally as possible and instead opt for running 'python3 src/static_update.py' to update the graphs on your local machine. There are very few reasons to actually run 'run.py' aside from explicitly updating the database.

There will be furthur documentation posted in the future on how exactly the codebase works and how its designed but for now this README should be enough to get started on developing and exploring the codebase. 
