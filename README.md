# 🚀 Loyalty Flow - Next-Gen Loyalty Program for Odoo POS

[![Odoo 17](https://img.shields.io/badge/Odoo-17-%23FF5722?logo=odoo)](https://www.odoo.com)
[![Docker](https://img.shields.io/badge/Docker-✓-2496ED?logo=docker)](https://www.docker.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Transform static loyalty points into dynamic tokens with AI-driven rewards and smart contracts!**  
Loyalty Flow gamifies customer engagement and sales performance directly within Odoo POS. 💸✨

---

## 📌 Features

- **Dynamic Tokens**: Earn, stake, and burn tokens for rewards (1 token = $1 spent).
- **AI-Powered Discounts**: Personalized offers based on purchase history.
- **Smart Contracts**: Code-driven rewards with zero fraud (no blockchain PhD needed!).
- **Sales Leaderboards**: Gamify team performance with token-based incentives.
- **Real-Time Dashboard**: Track token distribution, ROI, and customer behavior.

---

## 🎥 Demo

**Watch a Quick Demo**: [Loyalty Flow Demo Video](https://drive.google.com/drive/folders/1VSDrgBcm2XLStToNNlv99Q-dSQWUmadI?usp=drive_link)
**Live Demo Setup**:
```bash
git clone https://github.com/your-repo/loyalty-flow.git
cd loyalty-flow
docker-compose up
```
Access Odoo at `http://localhost:8069` and install the **Loyalty Flow** module.

---

## 🛠️ Installation

### Prerequisites
- Docker
- Docker Compose

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/loyalty-flow.git
   cd loyalty-flow
   ```
2. **Start Services**:
   ```bash
   docker-compose up
   ```
3. **Configure in Odoo**:
   - Create a database.
   - Install the **Loyalty Flow** module under **Apps**.
   - Link the loyalty program to POS under **Point of Sale → Configuration**.

---

## 🧑💻 Usage

### For Customers
1. **Earn Tokens**: Spend $100 → Get 100 tokens.
2. **Stake Tokens**: Stake 50 tokens → Unlock 5% discount.
3. **Redeem**: Apply discounts automatically at checkout.

### For Merchants
1. **Configure Programs**: Set token tiers (e.g., 100 tokens = 10% off).
2. **Track Analytics**: View token usage and ROI in the admin dashboard.

### For Sales Teams
1. **Earn Tokens**: Hit sales targets → Earn bonus tokens.
2. **Compete**: Climb leaderboards and redeem tokens for cash or perks.

---

## 🧩 Tech Stack

| **Area**       | **Tools**                                                                 |
|----------------|---------------------------------------------------------------------------|
| Backend        | Odoo 17, Python                                                          |
| Frontend       | Odoo Web, JavaScript, XML/QWeb                                           |
| AI Integration | Python, scikit-learn (mock rules for MVP)                                |
| Deployment     | Docker, Docker Compose                                                   |

---

## 🤝 Contributing

We welcome contributions!  
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-idea`.
3. Commit changes: `git commit -m 'Add awesome feature'`.
4. Push to the branch: `git push origin feature/your-idea`.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- **Team**: [Abhimanyu Ajudiya](), [Neha Kanabar](), [Jeet Bhensdadia]()  
- **Odoo Community** for the amazing framework.  
- **Hackathon Judges** for this opportunity!

---

Made with ❤️ during the [Hackathon Name]. Let’s make loyalty exciting again! 🚀


---

### 🌟 Key Enhancements
- **Visual Appeal**: Emojis, badges, and clean tables for readability.
- **Clear Sections**: Demo, installation, usage, and tech stack are separated for clarity.
- **Call to Action**: Contribution guidelines and acknowledgements encourage community involvement.
- **Mobile-Friendly**: Markdown formatting works well on all devices.

**Tip**: Add screenshots of the POS interface and dashboard under the `Demo` section for extra polish! 📸
