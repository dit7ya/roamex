export const getNormalizedUrl = (url) => {
  const normalizedUrl = new URL(url);
  normalizedUrl.hash = "";
  return normalizedUrl;
};
