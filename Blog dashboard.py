blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

trending_posts = 0

for x in blog_views:
    if x > 1000:
        print("Trending")
        trending_posts = trending_posts + 1
    elif x >= 500:
        print("Average")
    else:
        print("Low Traffic")

print("Total Views:", sum(blog_views))
print("Trending Posts:", trending_posts)