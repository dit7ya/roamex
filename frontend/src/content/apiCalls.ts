import axios, { AxiosResponse } from "axios";
import type { HighlightType, PageType, AnnotationType } from "./models";
import { getNormalizedUrl } from "./utils";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

const responseBody = (response: AxiosResponse) => response.data;

const requests = {
  get: (url: string) => instance.get(url).then(responseBody),
  post: (url: string, body: {}) => instance.post(url, body).then(responseBody),
  put: (url: string, body: {}) => instance.put(url, body).then(responseBody),
  delete: (url: string) => instance.delete(url).then(responseBody),
};

// Create a Page object with methods
// We are also normalizing the Page URL for both read and create here

export const Page = {
  // TODO if the page does not exist then the return type is something else
  readPage: (url: string): Promise<PageType> => {
    const normalizedUrlString = getNormalizedUrl(url).toString();
    return requests.get(`pages/?url=${normalizedUrlString}`);
  },

  createPage: (page: PageType): Promise<any> => {
    const normalizedUrlString = getNormalizedUrl(page.url).toString();
    page.url = normalizedUrlString;
    return requests.post("pages", page);
  },

  createOrUpdatePageComment: (
    pageId: string,
    pageComment: string
  ): Promise<any> => {
    return requests.put(`pages/${pageId}`, { text: pageComment }); // FIXME better model
  },
};

// Create a Highlight Object with methods
export const Highlight = {
  createHighlight: (highlight: HighlightType): Promise<any> =>
    requests.post("highlights", highlight),
  getHighlights: (pageId: string): Promise<HighlightType[]> =>
    requests.get(`highlights/${pageId}`),
  deleteHighlight: (highlightId: string): Promise<any> =>
    requests.delete(`highlights/${highlightId}`),
};

// Create an Annotation Object with methods

export const Annotation = {
  createAnnotation: (annotation: AnnotationType): Promise<any> =>
    requests.post("/annotations", annotation),
};

// TODO HACK REVIEW
export const getOrgRoamNodes = () => requests.get("/orgRoamNodes");
