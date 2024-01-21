Postmortem Report

Platform Crashing as more users access it.

Issue Summary: On the 15th of November 2023, we had user platform show and all of a sudden, we started experiencing error 500 with the status Internal Server Error.

Duration:

> 19h00 SAST: 200 users logged into the platform all at once.

>19h10 SAST: The site was failing to process requests for some users.

>19h11 SAST: Newer users couldn’t log into their accounts.

>19h15 SAST: Everyone started getting error 500 “Internal Server Error”.

>19h18 SAST: we logged 50% of online users out using our admin dashboard and the platform started to relatively perform better.

>19h20 SAST: we logged everyone in and the site crashed again.

>19h30 SAST: sent our users notifications that the site would be down for 24hours.

Root Cause:

The issue was with our infrastructure particularly our servers, we were using digitalocean servers which were under the basic plan. The servers had 512mb or RAM. The main issue here was that our platform couldn’t handle that many requests and that the current plan we were using was good for prototyping and not meant for scalability.

Resolution:

Since we are a very small platform we don’t have the luxury of using proper architecture such as additional servers, so we opted for a AWS VPS that consisted of 16gb of RAM and 2 TB worth of storage. For our small number of users this solution was sufficient enough and now we can handle even a bit more load than last time. In addition to this solution we started compressing file transfers, using CDNs, and some functions are peer to peer to reduce server requests.

Corrective and preventative measures must contain:

> Using load balancers.

> Enabling effective browser caching mechanisms.

> Investing in server spaces as we scale.
