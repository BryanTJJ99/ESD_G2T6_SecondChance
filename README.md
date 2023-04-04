# Hey there! Welcome to SecondChance.

### Motivation [Sustainability - Tanzu]
Large companies and institutions often waste budget by purchasing resources that already exist within their
organisation. This occurs due to a coordination problem, where departments working in silos do not know if other
departments have the required resources before making a purchase.

To tackle this issue, SecondChance offers a resource management platform that helps large organisations close the
circular loop by tracking and reusing existing resources within the company. The platform includes a range of items
such as furniture and medical equipment, among others. By doing so, SecondChance solves the coordination
problem and reduces business costs by avoiding the purchase of existing items in the inventory. Additionally, this
approach contributes to the organisation's sustainability goals by creating an internal circular economy.

The Carbon Retriever is designed to recover the quantity of carbon that is conserved through recycling each item
through the transfer of ownership. The cumulative reduction in carbon emissions for each department in each
organisation will be recorded. In today’s world where companies are striving to be sustainable and eco-friendly,
organisations will be able to incorporate the data into their annual report to not only to appear more accountable for
their existing customers but also to entice potential customers. 

Some of the features available in this application include:
Login & Verification to track organisation and department
Marketplace
Chat functionality between sender and receiver
Slack chatbot → Department make request for something, send to slack channel
Inventory Management



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

