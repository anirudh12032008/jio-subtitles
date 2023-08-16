import os
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 


def seconds_to_time_format(seconds):
    return str(timedelta(seconds=seconds))


def extract_subtitle(url, num_iterations,buffer):
    try:
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome( options=chrome_options)        
        driver.get(url)
        time.sleep(buffer)
        print("Subtitle:")
        all_subtitles = ""
        episode_title_element = driver.find_element(By.CSS_SELECTOR, "h1.MuiTypography-root")
        episode_title = episode_title_element.text.strip()
        previous_subtitle = ""
        for iteration in range(1, num_iterations + 1):
            try:
                subtitle_element = driver.find_element(By.CSS_SELECTOR, "span[style*='white-space: pre-wrap; color: white; direction: ltr;']")
                subtitle_text = subtitle_element.text 
                if subtitle_text != previous_subtitle:
                    time_text = seconds_to_time_format(iteration)

                    all_subtitles += f"{time_text} \n {subtitle_text} \n \n"
                    previous_subtitle = subtitle_text
                time.sleep(0.5)
            except NoSuchElementException:
                
                time.sleep(0.5)
                continue
        # Close the browser
            time.sleep(0.5)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        
        with open(f"{episode_title}.srt", "w", encoding="utf-8") as file:
            file.write(all_subtitles)

if __name__ == "__main__":
    video_url = input("Enter the link of video (ex:-  https://www.jiocinema.com/tv-shows/naagin/6/pragati-learns-prathna-s-past/3761450) :") 
    num_iterations = int(input("Enter the duraration of video (in sec): ")) 
    buffer = int(input("Enter the buffer duraration (in sec, if you don't know put 10): "))

    print("Starting subtitle extraction...")
    extract_subtitle(video_url, num_iterations, buffer)
    print("Subtitle extraction complete.")
