---
title: Contact
date: 2022-10-24

type: landing

sections:
  - block: markdown
    content:
      title:
      subtitle: ''
      text: |
        <!-- Contact form using Formspree -->
        <form
          action="https://formspree.io/f/mbjwlgow"
          method="POST"
        >
          <label>
            Your email:
            <input type="email" name="email">
          </label>
          <label>
            Your message:
            <textarea name="message"></textarea>
          </label>
          <!-- your other form fields go here -->
          <button type="submit">Send</button>
        </form>
    design:
      columns: '1'
      background:
        image: 
          filename: contact.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
