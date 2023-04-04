# Hey there! Welcome to SecondChance.

### 🔧 Setting up
1️⃣ Clone the repository from GitHub to your `desired_folder_name`
```bash
git clone https://github.com/BryanTJJ99/ESD_G2T6_SecondChance.git
```
<br></br>

### 🔧 Running the application
2️⃣ Navigate to the frontend folder ~/frontend. Run
```bash
npm i
npm run dev
```
<br></br>

3️⃣ Nagivate to the backend folder in another terminal ~/backend. Run
```bash
cd slack
python app.py
cd ..
docker-compose up
cd kong
docker-compose up
cd ..
``
Do note that we must add the app.py IP Address as the new Slack URL in the accept_item.py complex microservice.

<br></br>

### Technical Overview Diagram
https://drive.google.com/file/d/1NbS-Ss2NcYY7CVrgk80guPzbZnv-6uvq/view?usp=sharing

### API Documentation
https://drive.google.com/drive/folders/1Sc4srQExVhnRr5gXJ7wdEYfiGtiaHUi9?usp=sharing

### Troubleshooting
If npm run dev does not work - https://github.com/vuejs/vue-cli/issues/332

### Optional - Installation
How to install Docker: https://www.docker.com/products/docker-desktop/

