// Chat completion with the OpenAI Node SDK against the QuantoPort gateway.
//
//   npm install openai
//   export QP_API_KEY="sk-..."
//   node node_openai.mjs

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.QP_API_KEY,
  baseURL: process.env.QP_BASE_URL ?? "https://console.quantoport.com/v1",
});

const resp = await client.chat.completions.create({
  model: process.env.QP_MODEL ?? "deepseek-v4.1-flash",
  messages: [{ role: "user", content: "Say hello in five words." }],
});

console.log(resp.choices[0].message.content);
