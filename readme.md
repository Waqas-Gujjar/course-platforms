

---

# **Course Platform**  

A **Django-based** course platform using **HTMX, Cloudinary, Tailwind CSS, and Flowbite** for a dynamic and responsive UI.  

## **Features**  
✅ User authentication (Login/Logout)   
✅ Upload and manage course content using **Cloudinary**  
✅ Interactive UI with **HTMX** for seamless page updates  
✅ Modern styling with **Tailwind CSS** and **Flowbite components**  

## **Technologies Used**  
- **Backend:** Django, Python 
- **Frontend:** HTML, Tailwind CSS, Flowbite, HTMX  
- **Media Storage:** Cloudinary  
- **Database:** SQLite 
- **Authentication:** Django’s built-in auth system  

## **Installation & Setup**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/Waqas-Gujjar/course-platform.git
cd course-platform
```

### **2. Create Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4. Configure Cloudinary**  
Create a `.env` file and add:  
```sh
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### **5. Run Migrations**  
```sh
python manage.py migrate
```

### **6. Start Development Server**  
```sh
python manage.py runserver
```
Access the project at `http://127.0.0.1:8000/`  

## **Screenshots**  
_Add UI screenshots here_  

## **Deployment**  
You can deploy using **Vercel, Render, or DigitalOcean**.  

## **Contributing**  
1. Fork the repo  
2. Create a feature branch (`git checkout -b feature-xyz`)  
3. Commit changes (`git commit -m "Added feature xyz"`)  
4. Push to GitHub (`git push origin feature-xyz`)  
5. Open a Pull Request  



---

