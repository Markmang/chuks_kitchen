# Chuks Kitchen Backend API

### Internship Project -- Trueminds Innovations

------------------------------------------------------------------------

# 📌 Project Context

This backend system was developed as part of the **Trueminds Innovations
Internship Assessment**.

Chuks Kitchen is launching a food ordering platform.\
The goal of this project is to design and document the backend
architecture, API structure, and system logic that powers the platform.

This project focuses strictly on backend logic as required in the
internship brief.

------------------------------------------------------------------------

# 🏗 System Overview (End-to-End)

The system supports two roles:

## 1️⃣ Customer

-   Sign up (Email or Phone)
-   Verify account via OTP
-   Browse food
-   Add to cart (conceptual flow)
-   Place orders
-   Track order status

## 2️⃣ Admin (Chuks Kitchen Team)

-   Add / update food items
-   Update prices
-   Mark items unavailable
-   Manage orders

------------------------------------------------------------------------

# 🔌 Implemented API Endpoints

## Authentication & Registration

    POST /signup
    POST /verify

## Foods

    GET /foods
    POST /foods        (Admin)

## Orders

    POST /orders
    GET /orders/<int:pk>

------------------------------------------------------------------------

# 🔄 Backend Flow Diagrams

Below are high-level backend logic diagrams.

------------------------------------------------------------------------

# 1️⃣ User Registration Flow

## Flowchart

    User → POST /signup
            |
            V
    Validate email/phone uniqueness
            |
    Generate OTP
            |
    Store user (inactive)
            |
    Return "OTP Sent"

## Verification Flow

    User → POST /verify
            |
            V
    Validate OTP
            |
    If valid → Activate user
    If invalid → Return error

------------------------------------------------------------------------

# Data Required (Signup Screen)

    {
      "email": "user@example.com" OR "phone": "080xxxxxxx",
      "password": "securepassword",
      "referral_code": "optional"
    }

------------------------------------------------------------------------

# Edge Cases Handled

-   Duplicate email/phone → validation error
-   Invalid referral code → rejection
-   Expired OTP → verification failure
-   Incorrect OTP → error response
-   Abandoned signup → inactive user remains unverified

------------------------------------------------------------------------

# 2️⃣ Food Browsing Flow

    Frontend → GET /foods
            |
    Backend fetches all available food
            |
    Return JSON list

## Data Returned

    [
      {
        "id": 1,
        "name": "Jollof Rice",
        "price": 2500,
        "available": true
      }
    ]

Admin can:

    POST /foods

To add or update food items.

------------------------------------------------------------------------

# 3️⃣ Order Creation Flow

    Customer → POST /orders
            |
    Validate user
            |
    Validate cart items
            |
    Calculate total price
            |
    Create Order record
            |
    Return order_id

------------------------------------------------------------------------

# Data Required (Place Order Screen)

    {
      "items": [
        {
          "food_id": 1,
          "quantity": 2
        }
      ]
    }

------------------------------------------------------------------------

# 4️⃣ Order Detail Flow

    Customer → GET /orders/<id>
            |
    Validate ownership
            |
    Return order details + status

------------------------------------------------------------------------

# 📡 How Frontend Communicates with Backend

Conceptually:

-   Frontend sends HTTP requests (JSON format)
-   Backend validates input
-   Backend processes business logic
-   Backend returns JSON response
-   Frontend updates UI accordingly

Communication style: RESTful JSON API over HTTP

------------------------------------------------------------------------

# 🧠 Flow Explanation & Design Decisions

### Why OTP Verification?

-   Ensures valid user contact
-   Prevents fake registrations
-   Matches internship requirement

### Why Separate Food & Orders Endpoints?

-   Clear separation of responsibility
-   Clean REST design
-   Easier scalability

### Why Calculate Price in Backend?

-   Prevents price manipulation
-   Maintains integrity of transactions

------------------------------------------------------------------------

# ⚠ Edge Case Handling (Full System)

1.  Invalid or expired OTP → 400 error
2.  Duplicate email/phone → blocked
3.  Food marked unavailable → cannot be ordered
4.  Empty order → rejected
5.  Unauthorized order access → denied
6.  Admin-only actions → restricted

------------------------------------------------------------------------

# 📌 Assumptions

Due to limited product details, the following assumptions were made:

1.  OTP is simulated (no real email integration).
2.  Referral codes are validated if provided.
3.  Only verified users can place orders.
4.  Payment processing is out of scope.
5.  Single order status lifecycle (Pending → Completed).

------------------------------------------------------------------------

# 🚀 Scalability Thoughts (100 → 10,000+ Users)

If user base increases significantly:

## Database Improvements

-   Add indexes on email, phone, foreign keys
-   Move to PostgreSQL
-   Optimize queries

## Caching

-   Redis for food list caching
-   Reduce DB load

## Background Jobs

-   Use Celery for OTP handling
-   Order notifications

## Microservice Evolution

Future split: - Auth Service - Food Service - Order Service

## Production Readiness

-   Use .env for secrets
-   Environment-specific configs
-   Proper logging & monitoring

------------------------------------------------------------------------

# 🎯 Conclusion

This backend system demonstrates:

-   RESTful API design
-   Role-based system thinking
-   OTP verification flow
-   Order processing logic
-   Edge case planning
-   Scalability awareness

Developed as part of the **Trueminds Innovations Internship Backend
Assessment**.
