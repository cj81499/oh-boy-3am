function envGetOrThrow(key: string): string {
  const val = Deno.env.get(key);
  if (val === undefined) {
    throw new Error(`${key} is unset`);
  }
  return val;
}

export const MASTODON_SERVER_URL = envGetOrThrow("MASTODON_SERVER_URL");
export const MASTODON_API_TOKEN = envGetOrThrow("MASTODON_API_TOKEN");
