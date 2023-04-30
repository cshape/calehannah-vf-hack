"Mary Maker" 

- An AI wedding planner which saves you time researching and corresponding with vendors. 
- A delightful, useful conversational experience 
- Integrations with Google Sheets, Pinterest, Email
- Communicates through Website Chat as POC (but ideally through many channels)

*To Run the App*

1. `pip install Flask`
2. `pip install gunicorn`
3. `pip install googlesearch-python`
4. `gunicorn wsgi:app`

TODOS:

- [ ] Build Basic Bot flow in Voiceflow to facilitate convo
- [x] Figure out user experience/bot functionality long term
- [x] Figure out user experience/bot functionality to build today
- [ ] Connect to Voiceflow via API
- [ ] Connect to OpenAI via API
- [ ] Figure out good prompts and prompt chaining setup
- [ ] Connect to Google
- [ ] Connect to Email
- [ ] Use GPT-2 token counting API to have more graceful prompt/response limits
- [ ] Connect to DB
- [ ] Build logic for searching DB vs Google for longer-term planning
- [ ] Plug into image gen or image understanding tools to do cool stuff

*Long Term*

- Communicate thru email over months planning the wedding. Sends emails either a daily digest or maybe whenever vendors write back
- Can handle many aspects of organizing the wedding, from comms, to finances, to whatever

*Todays Demo*

- Collects important info to construct persona for the wedding couple
- Collects info on venue needs/wants/restrictions
- Searches for good venues matching those things
- Offers to contact the venues and set up a booking or viewing
- Emails the venues to start a convo with them, CCing the couple
