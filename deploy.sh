#!/bin/bash
gcloud builds submit --tag gcr.io/cdn-dinoia/feecalculator
gcloud run deploy --image gcr.io/cdn-dinoia/feecalculator --platform managed
