# Hotel Booking Cancellation Capstone Project 3
### by Dhiya Ilham - Purwadhika Data Science & Machine Learning Bootcamp
Linkedin: https://www.linkedin.com/in/dhiya-ilhamtri/

Youtube: https://youtu.be/niiBfG-iqgY?si=tiJx_-OFg-MQIaMm

Portfolio: https://s.id/IlhamDSPortfolio (This Slide on this link)

# Business Understanding

## Introduction

In the hospitality industry, especially hotels, overbooking is a common strategy to handle booking cancellations. With the rise of online platforms, it has become easier for customers to make and cancel reservations.

Booking cancellations can significantly impact hotel operations. While they can help maximize revenue through overbooking, they also pose a risk to the hotel’s reputation if not managed properly. Therefore, if hotels can predict cancellations in advance, they can better optimize their overbooking strategies and minimize potential risks.

## Problem Statement

Overbooking strategies work best when we can estimate how many bookings are likely to be canceled. If we underestimate cancellations, more rooms may end up empty and unused. But if we overestimate cancellations, we risk having too many guests and not enough rooms, which can lead to customer dissatisfaction due to overbooking.

That’s why accurate cancellation prediction is key to balancing occupancy and guest satisfaction.

## Project Goals

Based on the problem statement, the goal is to accurately predict whether a booking will be canceled or not. This helps in making better decisions and supports the overbooking strategy.

We may also discover certain booking characteristics that are strongly linked to cancellations, which can help identify which reservations are more likely to be canceled.

## Analytical Approach

Based on the problem statement, the goal is to accurately predict whether a booking will be canceled or not. This helps in making better decisions and supports the overbooking strategy.

We may also discover certain booking characteristics that are strongly linked to cancellations, which can help identify which reservations are more likely to be canceled.

## Evaluation Metrics

Target (y):
- 0 : Not Canceled
- 1 : Canceled

Confusion Matrix:

| Actual/Predicted | Negative (0/Not Canceled) | Positive (1/Canceled) |
| --- | --- | --- |
| Negatif (0) | Actual not canceled, predicted not canceled (True Negative / TN)  | Actual not canceled, predicted canceled (False Positive / FP) |
| Positive (1) | Actual canceled, predicted not canceled (False Negative / FN) | Actual canceled, predicted canceled (True Positive / TP) |


False Negative (FN) : 

The model predicts a guest will show up, but they cancel.

→ The room goes unbooked and empty, even though another guest could have stayed.

False Positive (FP) : 

The model predicts a cancellation, but the guest actually shows up.

→ The hotel becomes overbooked, risking customer dissatisfaction and damaging the hotel’s reputation, the guest may not return in the future.

This is the the research of overbooking and minimize cost strategies

Source: https://oaky.com/en/blog/hotel-overbooking

**Is overbooking a good practice for hotels [Pros and cons of hotel overbooking]**

Pros of hotel overbooking:

- Mitigates the risk of last-minute cancellations and no-shows
- Maximises occupancy
- Prevents revenue losses
- Lets you stay competitive on OTAs

Cons of hotel overbooking:

- Lost revenue opportunities
- Guest dissatisfaction and hotel reputational damage
- Inefficiencies and disruptions in hotel operations

Both types of prediction errors can negatively affect hotel revenue. However, in my opinion, overbooking (False Positive) is more harmful than an empty room (False Negative). Overbooking may lead to long-term revenue loss because dissatisfied guests who experience poor service are less likely to return. This damages the hotel’s reputation, which is a major concern.

While some might argue that overbooking is generally less costly than leaving rooms empty, in reality, overbooking often forces the hotel to cover extra costs, such as transportation or relocation to another hotel.

Therefore, overall, I believe overbooked rooms are more damaging than empty rooms, although both should be minimized.
To address this, I’ll use the F2 Score — a metric that still considers both precision and recall but places more weight on recall, which is more important in this case. I’ll also use ROC AUC Score as a secondary evaluation metric.
