# Anmeldunghunt

The script needs the URL for the appointment calendar page and a deadline date, which is the last day of the range of dates to check. The script will check all dates from 'tomorrow' until the deadline date.

Leave it running and when an appointment that fits the range is found, it will play a sound and open the browser for you to fill in your details to book the appointment.

## Usage
Install requirements:
```python3 -m install -r requirements.txt```

Update the variables ```url``` and ```deadline``` in the script.

Run the script: ```python3 anmeldunghunt.py```
