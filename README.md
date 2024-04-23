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

### Login screen and operations

When the application is launched, you will be greeted with a user interface. In this interface, you will need to input your email and password in the designated fields. After entering this information, upon clicking the 'Sign In' button, the application will first verify the correctness of your email and password in the background. At this stage, the application utilizes the Selenium library to ensure accuracy.

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232309636305125416/Login_Screen.PNG?ex=6628fd48&is=6627abc8&hm=5341f06e2786d68102ea092f2882515b989219dec5432a5f3844119ca1b41e07&" alt="Login Screen">
</p>

---

### Step 1: Email - Password Verification

In this step, we verify the correctness of the email and password used to log in to the Sellerflash application. If the login is successful, we proceed to the next step by receiving the result "True" in the terminal.

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232317096441155715/Selenium1.PNG?ex=6629043b&is=6627b2bb&hm=8fb6bbebe0738f3a533bcf939398504c44dae18b2743cc1a5db816c72ff39e30&" alt="Login Screen">
</p>

---

### Step 2: Username, Product Limit, Product Count

In this step, after verifying the email and password, we gain access to the username, product limit, and the number of products found. This ensures scanning the correct number of products and prevents exceeding the account quota.

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/782962565293932554/1232321304473112687/Selenium2.PNG?ex=66290826&is=6627b6a6&hm=14086d9ea592e7759e02df8563f48fb3ce271c1c6927533faf38fa507d54afd5&" alt="Login Screen">
</p>
