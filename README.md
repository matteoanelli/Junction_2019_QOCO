# QOCO Challenge - Junction 2019


## Problem

Airports, airlines, and airport logistics companies can cause a lot of anger to their customers by loosing or damaging their baggage. There are 3 main points where the baggage can be lost are :
	
* Lost baggage tag
* Loading baggage on wrong flight
* Connecting flights have baggage delay

Baggage can be damaged at each loading and unloading of the baggage
 
## Solution

Our solution goes over each of the problem points stated in the previous section

### Lost baggage tag

As the baggage tag is lost, the only way to discover the owner is by using description data about the baggage and a process of elimination, or by waiting for a customer report. In our solution the customer does not receive their luggage at the baggage claim and scans a QR code, this leads them to a chatbot, they fill in their baggage claim number and get information on when and how they will get their luggage along with some vouchers for clothing stores or restaurants when applicable.

### Loading baggage on wrong flight

In the future, this will be solved by a more smart solution that scans each luggage before it is loaded on the airplane. Until then, the solution for the lost baggage tag will offer a solution to this problem.

### Connecting flights have baggage delay
In this case, the customer will be notified by an email or SMS message with information about their luggage and that it will be delayed. This email will contain a link to track the status of the baggage and ask necessary questions. Once the baggage arrives at the airport, the user will get another email to inform them the baggage has arrived, and how to pick it up.

### Damaged baggage
If the user notices some damage to the baggage at the baggage claim, they can scan the QR code located next to the baggage claim to report the issue. This will link them to another chat-bot, which will authenticate the baggage and ask the owner about the problem and instruct them how and if they will get reimbursed for the damages.

## Data used
The data used will be from the Qoco API. This API gives data on baggage, customers, and baggage events. 
### Baggage data
This holds information on the baggage type, physical description, and status.
### Customer data
This holds information on name, contact information, travel itinerary, and owned baggage
### Baggage events
This holds information on whether the baggage is claimed, loaded, unloaded, checked, damaged, or missing