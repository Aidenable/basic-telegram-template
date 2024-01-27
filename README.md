![Banner](/public/github-banner.png)

# AIOgram [v2.22] Template

Template for telegram bots with minimal functionality

### What is included in this template?
- 🍃 [**MongoDB**](https://www.mongodb.com/) - Comfortable working with models; de/serialization; FSM manager; etc.
- 🗑️ **Memory Cache** - Integrated memory system in the database.
- 📦 **Router** - No dependency on dispatcher; also grouping of handlers into a unit.
- 🔗 **Starter Manager** - Easy work with referral links or something similar.
- 💢 **Triggers** - Like [`logging`](https://docs.python.org/3/library/logging.html), but a bit cooler.
- ⏲️ **Background Tasks** - Just an [`apscheduler`](https://apscheduler.readthedocs.io/en/3.x/userguide.html).


### What will NOT be included in this template? 
> *Because it's in my **PRO**-template*
1. i18n
2. [Redis](https://redis.io/)
3. Pagination
4. Payment Systems
5. [WebApp](https://core.telegram.org/bots/webapps)

## Instruction
1. Clone this repository:
```
git clone git@github.com:Aiden-The-Dev/basic-telegram-template.git
cd basic-telegram-template
```
---

2. Next, install the required packages using [`poetry`](https://python-poetry.org/):
```
poetry install
```
2. Or install the packages using pip:
```
pip install -r requirements
```

---

3. Use the command to run the program:
```
poetry run python main.py
```

---

4. If you want to run the program at boot time, use systemd on Linux:
```
cp /etc/systemd/system/ bot.service
sudo systemctl start bot.service
```
