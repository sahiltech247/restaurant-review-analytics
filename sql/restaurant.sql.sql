create database restaurant;
use restaurant;
SELECT * FROM restaurant_tb;

#---[1]Find the total number of reviews in the dataset.
SELECT COUNT(*) AS total_reviews
FROM restaurant_tb;
#---[2]Count how many reviews belong to each sentiment category.
select sentiment, count(sentiment) as count from restaurant_tb
group by sentiment;
#---[3]Find the average overall rating of the restaurants.
select round(avg(overall_rating)) as avg_rating from restaurant_tb;
#---[4]Show the number of reviews in each review category.
select category, count(category) as count from restaurant_tb
group by category;
#---[5]Find all reviews where: sentiment is Negative and rating is 1 or 2
select clean_review, sentiment, Overall_Rating from restaurant_tb
where sentiment = "Negative" AND Overall_Rating in (1, 2);
#---[6]Calculate the percentage of positive, negative, and neutral reviews.
select sentiment, count(*) as total_reviews, 
round(count(*) * 100.0/ (select count(*) from restaurant_tb),2)
as percentage from restaurant_tb
group by sentiment;
#---[7]Find which category has the highest number of negative reviews.
select category, count(*) as neg_review from restaurant_tb
where sentiment = "Negative"
group by category
order by neg_review desc
limit 1;
#---[8]Restaurant with highest orders
select name, count(*) as highest_orders from restaurant_tb
group by name
order by highest_orders desc
limit 1;
#---[9]Restaurant with Loweest orders
select name, count(*) as Lowest_orders from restaurant_tb
group by name
order by lowest_orders
limit 1;
#---[10]Restaurant with highest orders with highest ratings
select Name, count(*) as total_orders, round(avg(overall_rating), 2) 
as avg_rating from restaurant_tb
group by Name
having count(*)>5
order by avg_rating desc
limit 5;
#---[11]City with highest orders
select city, count(*) as total_orders from restaurant_tb
group by city
order by total_orders desc
limit 3;
#---[12]City with lowest orders
select city, count(*) as total_orders from restaurant_tb
group by city
order by total_orders 
limit 3;
