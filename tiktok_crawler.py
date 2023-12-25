from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get(
    "ms_token",
)  # set your own ms_token, think it might need to have visited a profile


async def user_example():
  async with TikTokApi() as api:
    await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False,
                                override_browser_args=["--incognito"])
    user = api.user("lazadavietnam")
    user_data = await user.info()
    with open("tiktok_lzd_data.csv", "w", encoding='utf-8') as f:
        header_labels = "Create_time,Create_year,Create_month,Create_day,Create_hour,Likes,Comments,Saves,Views,Shares,Duration(sec),Video Height,Video Width\n"
        f.write(header_labels)
        async for video in user.videos(count=3000):
            create_time = str(video.create_time)
            video_data = {
                "Create_time": video.create_time,
                "Create_year": create_time[0:4],
                "Create_month": create_time[5:7],
                "Create_day": create_time[8:10],
                "Create_hour": create_time[11:13],
                "Likes": video.stats["diggCount"],
                "Comments": video.stats["commentCount"],
                "Saves": video.stats["collectCount"],
                "Views": video.stats["playCount"],
                "Shares": video.stats["shareCount"],
                "Duration(sec)": video.as_dict["video"]["duration"],
                "Video Height": video.as_dict["video"]["height"],
                "Video Width": video.as_dict["video"]["width"],
            }
            row = f'{video_data["Create_time"]},"{video_data["Create_year"]}","{video_data["Create_month"]}","{video_data["Create_day"]}","{video_data["Create_hour"]}","{video_data["Likes"]}","{video_data["Comments"]}",{video_data["Saves"]},{video_data["Views"]},{video_data["Shares"]},{video_data["Duration(sec)"]},{video_data["Video Height"]},{video_data["Video Width"]}\n'
            f.write(row)

if __name__ == "__main__":
  asyncio.run(user_example())