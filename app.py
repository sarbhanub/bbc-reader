import os
from flask import Flask, render_template, request
from src.mongoconnect import connect, close
from datetime import datetime, timedelta

app = Flask(__name__)

categories = {
    "top_stories": "Top Stories",
    "world": "World",
    "uk": "UK",
    "business": "Business",
    "politics": "Politics",
    "health": "Health",
    "education": "Education",
    "science_environment": "Science & Environment",
    "technology": "Technology",
    "entertainment_arts": "Entertainment & Arts"
}

continents = {
    "africa": "Africa",
    "asia": "Asia",
    "europe": "Europe",
    "latin_america": "Latin America",
    "middle_east": "Middle East",
    "north_america": "North America"
}

# fetch data from upto 3 days
today = datetime.utcnow()
daysbefore = today - timedelta(days=3)

# formatting published date for index
@app.template_filter("datetimeformat")
def datetimeformat(value):
    if isinstance(value, str):
        value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    current_time = datetime.now()
    time_difference = current_time - value

    if time_difference.days > 0:
        return f'{time_difference.days} {"day" if time_difference.days == 1 else "days"} ago'
    elif time_difference.seconds // 3600 > 0:
        hours = time_difference.seconds // 3600
        return f'{hours} {"hour" if hours == 1 else "hours"} ago'
    elif time_difference.seconds // 60 > 0:
        minutes = time_difference.seconds // 60
        return f'{minutes} {"minute" if minutes == 1 else "minutes"} ago'
    else:
        return "Just now"


@app.route("/")
def index():
    selected_category = request.args.get("category", "top_stories")

    # Establish the database connection
    client = connect(os.environ.get("URI_SECRET"))
    prod_db = client["newsdb-prod"]
    sent_db = client["sentdb-prod"]
    news_col = prod_db["newscol"]
    sent_col = sent_db["sentcol"]

    com_values = {}
    for item in sent_col.find({}, {"_id": 1, "compound": 1}):
        com_values[item["_id"]] = item["compound"]

    news_data = []

    # query
    articles = news_col.find(
        {
            "date_published": {"$gte": daysbefore, "$lt": today},
            "tags": {"$regex": f".*{selected_category}.*"}
        }
    )

    for article in articles:
        _id = article["_id"]
        title = article["title"]
        date_published = article["date_published"]
        description = article["description"]
        tags = article["tags"]
        guid = article["guid"]
        image_url = article["image_url"]

        com = com_values.get(_id, 0)
        if com <= -0.7:
            sentiment_class = "negative"
        elif com >= 0.7:
            sentiment_class = "positive"
        else:
            sentiment_class = "neutral"

        news_data.append(
            {
                "_id": _id,
                "title": title,
                "date_published": date_published,
                "description": description,
                "tags": tags,
                "guid": guid,
                "image_url": image_url,
                "sentiment_class": sentiment_class
            }
        )

    selected_sort = request.args.get("sort")

    sort_options = {
        "positive": lambda item: (
            item["sentiment_class"] != "negative",
            item["sentiment_class"] != "neutral",
            item["date_published"]
        ),
        "negative": lambda item: (
            item["sentiment_class"] != "positive",
            item["sentiment_class"] != "neutral",
            item["date_published"]
        ),
    }

    sort_key = sort_options.get(selected_sort, lambda item: item["date_published"])
    news_data.sort(key=sort_key, reverse=True)

    # Close the database connection
    close(client)

    return render_template(
        "index.html",
        continents=continents,
        categories=categories,
        data=news_data,
        selected_category=selected_category,
        selected_sort=selected_sort
    )


if __name__ == "__main__":
    app.run()
