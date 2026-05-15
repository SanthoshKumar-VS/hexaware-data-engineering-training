use("retail_project")

db.campaign_feedback.insertMany([{
        customer_name: "Rahul",
        product: "Laptop",
        feedback: "Good product",
        rating: 4
    },

    {
        customer_name: "Anjali",
        product: "Shoes",
        feedback: "Nice quality",
        rating: 5
    },

    {
        customer_name: "Kiran",
        product: "Mouse",
        feedback: "Average",
        rating: 3
    }
])

db.campaign_feedback.find()