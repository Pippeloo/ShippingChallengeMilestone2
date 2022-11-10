FROM nginx:stable-alpine

# Copy the frontend
COPY src /usr/share/nginx/html

# Expose the port
EXPOSE 80

# Run the app
CMD ["nginx", "-g", "daemon off;"]

