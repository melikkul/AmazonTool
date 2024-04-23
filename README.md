# AmazonTool

### Tools Used

The fundamental tools used in this project are listed below:

- **Selenium Library:** A library used for web automation.
- **Pandas Library:** A library used for data analysis and manipulation.
- **PySide6 Library:** A Python binding used for creating user interfaces.
- **Thread Library:** A library providing support for concurrent processes and multi-threading.
- **Time Library:** A library used for performing operations related to time.

These libraries are utilized in various aspects of the project, supporting different functionalities.

### What is Amazon Tool? What does Amazon tool do?

Amazon Tool is an automation tool designed for those interested in the Dropshipping (FBM) model within Amazon's business models and who use the Sellerflash Software. This tool monitors your Sellerflash membership, captures product ASIN (Amazon Standard Identification Number) information based on the limits of your package in the software, and uploads them to your store. Thus, it enhances the efficiency of your business on Sellerflash while allowing you to utilize your time more effectively.

---

### To-Do List:

This section lists the tasks to be completed for the project:

- **Detection of Asins:** Identifying and recording the Asins.
- **Transfer of Product Asins:** Transfer the identified product Asins to a new Excel file.
- **Loading Asins into Sellerflash Software:** Uploading the identified Asins into the Sellerflash software.
- **Modification of Necessary Informations on the Interface:** Updating the informative messages and texts on the interface.
- **Deletion of Products Based on Filter Settings:** Deleting products based on specific filter settings.
- **Navigating to the Next Link in Excel and Repeating the Process:** Proceeding to the next link in Excel and repeating the process.

---

### Current Issues:

This section lists the current issues with the project:

- **Unresponsive State of the Initial Interface While Selenium is Running:** Issues related to the initial interface becoming unresponsive while Selenium is running.

---

### Login screen and operations

When the application is launched, you will be greeted with a user interface. In this interface, you will need to input your email and password in the designated fields. After entering this information, upon clicking the 'Sign In' button, the application will first verify the correctness of your email and password in the background. At this stage, the application utilizes the Selenium library to ensure accuracy.

<details>
<summary><b><big>Click for image</big></b></summary>
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232309636305125416/Login_Screen.PNG?ex=6628fd48&is=6627abc8&hm=5341f06e2786d68102ea092f2882515b989219dec5432a5f3844119ca1b41e07&" alt="Login Screen">
</p>
</details>

---

### Step 1: Email - Password Verification

In this step, we verify the correctness of the email and password used to log in to the Sellerflash application. If the login is successful, we proceed to the next step by receiving the result "True" in the terminal.

<details>
<summary><b><big>Click for image</big></b></summary>
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232317096441155715/Selenium1.PNG?ex=6629043b&is=6627b2bb&hm=8fb6bbebe0738f3a533bcf939398504c44dae18b2743cc1a5db816c72ff39e30&" alt="Login Screen">
</p>
</details>

---

### Step 2: Username, Product Limit, Product Count

In this step, after verifying the email and password, we gain access to the username, product limit, and the number of products found. This ensures scanning the correct number of products and prevents exceeding the account quota.

<details>
<summary><b><big>Click for image</big></b></summary>
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232321304473112687/Selenium2.PNG?ex=66290826&is=6627b6a6&hm=14086d9ea592e7759e02df8563f48fb3ce271c1c6927533faf38fa507d54afd5&" alt="Login Screen">
</p>
</details>

---

### Step 3: File Location and Starting Product Scanning

In this step, a new interface greets us. In this interface, we can see the number of products in our store, the daily scanning limit, and our package limit. Additionally, in this section, there are three buttons: "Asin Folder", "Start", and "Stop". However, the "Stop" button is not yet functional. You must first press the "Asin Folder" button, otherwise you will see an error screen in the interface. After clicking the button, you will be prompted to select a file in Excel (.xlsx) format only. After selecting the file location, you will see the location in the interface. Upon pressing the "Start" button, the process will begin with the links found in the first row and column of the Excel file.

<details>
<summary><b><big>Click for image</big></b></summary>
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232324637036122153/Settings_Screen.PNG?ex=66290b40&is=6627b9c0&hm=5b5f749cd0dfbd33e2c8256b1a0ff26ef7b5ceabb78f793bfc960a2749edc43a&" alt="Login Screen">
  <p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232325360662614056/Settings_Screen1.PNG?ex=66290bed&is=6627ba6d&hm=e9928c7f3c5f61cc0ec2924f1b9978ca7c6b6faac6e317c1bc80bfba12a0edcd&" alt="Login Screen">
  <p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232325372570239106/Settings_Screen2.PNG?ex=66290bf0&is=6627ba70&hm=1b38764b1d3dc24253a29d1dc5255e3d8aedd78d5147646f5a035ba79442abb3&" alt="Login Screen">
</p>
</details>

---

### Step 4: Detection of Categories and Average Product Count

In this step, after entering the link found in our Excel file, the first action taken is to check the zip code. If the zip code is not "10001", actions are taken to correct it to "10001". Afterwards, once all products are accessed, the existing categories are identified. During this process, real-time information about these operations is displayed on our interface. After the category detection process is completed, the estimated product count in each category is determined. During this stage, the progress of the operation is displayed as a percentage on our interface. Additionally, information about the product count is also provided on the interface.

<details>
<summary><b><big>Click for image</big></b></summary>
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232329260606165082/Selenium4.PNG?ex=66290f8f&is=6627be0f&hm=5f77b26ab603b0e512404f2bce809b3e1e5e022ec4155eb7833d33973223b9d2&" alt="Login Screen">
  <p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232329275500265553/Selenium5.PNG?ex=66290f92&is=6627be12&hm=e7644b0acebabc50745fe393b5065b2ace880a822bd51aa004a85af09fce6a82&" alt="Login Screen">
</p>
</details>
