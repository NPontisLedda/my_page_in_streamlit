# My first page in Streamlit

This is my first project learning to use the Streamlit Python library.

To enter it, here I leave the entry [link](https://buttersweet.streamlit.app/).

This page is a first test project on the use of the Streamlit library, it is about an old pastry business that I had in 2020, when due to the COVID-19 pandemic, I had to leave the one in That was my job then.

I wanted to use my own images and everything to give a style to the page. He still has a lot to improve, but I keep practicing. It contains:

- A sidebar for selecting a specific page to view.
- Use of animations, they are loaded from [Lottie](https://lottiefiles.com/); To use the animations, it is necessary to have the streamlit-lottie library installed.
- A contact form, so that the person can make any possible queries. At the moment it has a classic Google form installed, but later, the idea is to change it and place one more in line with the design of the page.

## Technologies Used 🛠️

This project utilizes a combination of various libraries and technologies to create an interactive and visually appealing web application. Below is a breakdown of the key technologies used:

### Streamlit 👑
[Streamlit](https://streamlit.io/) is an open-source Python library that allows the creation of web applications for data science and machine learning projects. It is used as the primary framework for building the web interface of the application.

### Pillow
[Pillow](https://python-pillow.org/) is a Python Imaging Library (PIL) that adds image processing capabilities to your Python interpreter. In this project, Pillow is used to handle image loading and processing.

### Requests
[Requests](https://docs.python-requests.org/en/master/) is a simple and elegant HTTP library for Python. It is used in this project to fetch data from web URLs, such as images and JSON data for animations.

### streamlit-lottie
[streamlit-lottie](https://pypi.org/project/streamlit-lottie/) is a Streamlit component that allows the integration of Lottie animations into Streamlit apps. Lottie animations are high-quality, interactive animations that can be used to enhance the visual appeal of the application.

### Google Forms
The contact section of the application integrates a Google Form using an iframe. This allows users to submit their contact information directly through the web app, leveraging the simplicity and reliability of Google Forms.

### HTML/CSS
Custom HTML and CSS are used to style the application. The `css_load` function loads external CSS from a file to apply custom styles, enhancing the visual presentation of the app.


## Run Locally

### 1. Clone the project

```bash
  git clone https://github.com/NPontisLedda/my_page_in_streamlit.git
```

### 2. Go to the project directory

```bash
  cd my_page_in_streamlit
```

### 3. Run command to activate virtual environment

```bash
  venv/Scripts/activate.ps1
```

### 4. Start the server

```bash
  streamlit run app.py
```

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project or have suggestions, please follow these steps:

### 1. Fork the Repository

Click the "Fork" button on the top right of this page to create your own copy of the repository.

### 2. Create a New Branch

Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature
```

### 3. Make Your Changes

Make the necessary changes or additions to the codebase.

### 4. Commit Your Changes

Add and commit your changes:

```bash
git add .
git commit -m "Add a descriptive message about your changes"
```

### 5. Push to Your Fork

Push your changes to your forked repository:

```bash
git push origin feature/your-feature
```

### 6. Submit a Pull Request

Go to the original repository and submit a pull request with a clear description of your changes.

## 📞 Contact

If you have any questions or need further information, feel free to reach out:

- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/nicolas-pontis-ledda/)
- **Email**: nicopontis54@gmail.com
- **GitHub**: [NPontisLedda](https://github.com/NPontisLedda)


Thank you for checking out my project! I hope you find it useful and inspiring. Happy coding!