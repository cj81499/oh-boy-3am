import * as config from "./config.ts";
import { masto } from "./deps.ts";

console.log("Creating Mastodon client");
const mastodonClient = await masto.login({
  url: config.MASTODON_SERVER_URL,
  accessToken: config.MASTODON_API_TOKEN,
});
console.log("Created Mastodon client");

console.log("Uploading media");
const media = await mastodonClient.v2.mediaAttachments.create({
  file: new Blob([await Deno.readFile("./static/3am.mp4")]),
  description:
    'Patrick Star from the television show Spongebob Squarepants wakes up to an alarm clock and says "Oh boy, 3am!" before taking a bite of a Krabby Patty',
});
console.log(`Uploaded media (id: ${media.id})`);

console.log(`Posting status`);
const status = await mastodonClient.v1.statuses.create({
  status: "OH BOY 3AM!",
  visibility: "public",
  mediaIds: [media.id],
});
console.log(`Posted status (url: ${status.url})`);
