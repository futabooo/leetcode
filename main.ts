import puppeteer from "puppeteer";

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 1080 });
  await page.goto("https://leetcode.com/futabooo/", {
    waitUntil: "networkidle2",
  });
  const fileElement = await page.waitForSelector(".mx-auto");
  await fileElement?.screenshot({ path: "screenshot/score.png" });
  await browser.close();
})();
