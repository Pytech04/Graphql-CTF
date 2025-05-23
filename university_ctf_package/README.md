# 🎓 GraphQL IDOR CTF Challenge - University Deployment Guide

## 📋 Overview
This is a completely offline GraphQL IDOR (Insecure Direct Object Reference) CTF challenge designed for cybersecurity education. Perfect for university labs and Cisco CTF platforms.

## 🎯 Educational Objectives
- Learn GraphQL security fundamentals
- Understand IDOR vulnerabilities
- Practice API security testing
- Develop ethical hacking skills

## 🚀 Quick Deployment Options

### Option 1: Docker (Recommended for Universities)
```bash
# Build and run the challenge
docker build -t graphql-idor-ctf .
docker run -p 5000:5000 graphql-idor-ctf

# Or use docker-compose for production
docker-compose up -d
```

### Option 2: Python Direct Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 3: Standalone Executable (Coming Soon)
We can create a PyInstaller binary for complete offline distribution.

## 🌐 Access Points
- **Main Challenge**: http://localhost:5000
- **GraphQL Interface**: http://localhost:5000/graphql
- **Challenge Guide**: http://localhost:5000/challenge

## 🏆 Challenge Details

### Flag Location
- **Target**: User ID 3 (admin user)
- **Flag**: `CTF{graphql_idor_pwned_2024}`
- **Vulnerability**: Missing authorization on user queries

### Student Learning Path
1. **Discovery**: Use GraphQL introspection
2. **Reconnaissance**: Query current user context
3. **Exploitation**: Test IDOR vulnerability
4. **Extraction**: Retrieve admin user's flag

## 🔧 Customization for Your University

### Custom Flags
Edit `seed.py` to change the flag:
```python
'flag': 'YOURCOLLEGE{custom_flag_here}'
```

### Custom Branding
- Update templates in `/templates/` folder
- Modify university name and logos
- Add your cybersecurity department branding

### Difficulty Levels
- **Beginner**: Current setup (direct IDOR)
- **Intermediate**: Add rate limiting, obfuscated IDs
- **Advanced**: Add JWT authentication, complex authorization

## 📚 Instructor Resources

### Grading Rubric
- **Schema Discovery (25%)**: Student finds available queries
- **Vulnerability Identification (25%)**: Recognizes IDOR flaw
- **Exploitation (25%)**: Successfully accesses unauthorized data
- **Flag Extraction (25%)**: Retrieves the correct flag

### Common Student Mistakes
1. Not using introspection to discover schema
2. Only testing sequential user IDs (1, 2, 3...)
3. Missing the admin user with higher ID
4. Not understanding GraphQL syntax

## 🛡️ Security Notes for Instructors
- Challenge runs in isolated container
- No external network dependencies
- Safe for university lab environments
- Easy to reset between student sessions

## 📊 Integration with Cisco CTF Platform
- Standalone web application
- RESTful flag submission endpoint available
- JSON logging for automated scoring
- Easy integration with existing CTF infrastructure

## 🔄 Reset Instructions
```bash
# Reset database
docker-compose down
docker-compose up -d

# Or manually delete SQLite file
rm data/ctf_challenge.db
```

## 📞 Support
For university deployment support or customization requests, this challenge is ready for immediate classroom use!

---
**Perfect for**: Cybersecurity courses, ethical hacking labs, penetration testing training