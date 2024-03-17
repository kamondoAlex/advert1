def generate_welcome_page(Cashforclicks):
    # HTML content for the welcome page
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to {Cashforclicks}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-image: url('background_image.jpg'); /* Background image */
                background-size: cover;
                background-position: center;
                color: #fff;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                padding: 20px;
                text-align: center;
            }}
            h1, h2, p {{
                margin-bottom: 20px;
            }}
            .contact-info {{
                margin-top: 50px;
            }}
            .contact-info p {{
                margin-bottom: 10px;
            }}
            .reviews {{
                margin-top: 50px;
                text-align: left;
            }}
            .reviews p {{
                margin-bottom: 10px;
            }}
            .homepage-link {{
                display: inline-block;
                padding: 10px 20px;
                background-color: #007bff;
                color: #fff;
                text-decoration: none;
                border-radius: 4px;
                margin-top: 50px;
            }}
            .homepage-link:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to {Cashforclicks}</h1>
            <p>We are an innovative advertising company dedicated to helping businesses grow their brand and reach their target audience.</p>
            <div class="contact-info">
                <h2>Contact Us:</h2>
                <p>Email: kamondoalex@wgmail.com</p>
            </div>
            <div class="reviews">
                <h2>Positive Reviews:</h2>
                <p>"Great service! Highly recommend."</p>
                <p>"Excellent results. Will definitely use again."</p>
                <p>"Very professional team. Delivered as promised."</p>
            </div>
            <a href="https://www.yourhomepage.com" class="homepage-link">Visit Our Homepage</a>
        </div>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open('welcome.html', 'w') as file:
        file.write(html_content)

# Call the function to generate the welcome page
generate_welcome_page("Cashforclicks")
