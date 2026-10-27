# Best Cars Dealership Review Portal

Repository: `fullstack_dealer_capstone`

Project name: **Best Cars Dealership Review Portal**

A full-stack capstone application for finding U.S. car dealerships, reading customer reviews, and posting a review after signing in. The `server/frontend/static` directory contains the About and Contact pages. The React registration component is in `server/frontend/src/components/Register/Register.jsx`.

The Django service exposes authentication, dealership, car model, review, and sentiment endpoints. From the `server` directory, install `requirements.txt`, run `python manage.py migrate`, and then `python manage.py runserver`. The `/fetchDealers` endpoint returns the complete 50-record demo catalogue; `/analyze/Fantastic%20services` returns a positive sentiment result.

This repository was prepared for the IBM Full Stack Application Development Capstone Project. Screenshots and endpoint outputs should be captured from a running instance before submission.
