import normalizeUrl from "normalize-url";

export const getNormalizedUrl = (url) => {
  return normalizeUrl(url, {
    stripHash: true,
    stripProtocol: true,
    removeQueryParameters: ["ref"], // removing other paramaters is not a good idea
    sortQueryParameters: true,
  });
};
