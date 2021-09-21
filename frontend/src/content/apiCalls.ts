import axios, { AxiosResponse } from "axios";
import type { HighlightType, PageType, AnnotationType } from "./models";

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

export const Page = {
  readPage: (url: string) => requests.get(`pages/?url=${url}`), // FIXME URL

  createPage: (page: PageType): Promise<PageType> =>
    requests.post("pages", page),
  // TODO readPage
};

// Create a Highlight Object with methods
export const Highlight = {
  createHighlight: (highlight: HighlightType): Promise<HighlightType> =>
    requests.post("highlights", highlight),
  getHighlights: (
    pageId: string
    // ): Promise<HighlightType> => // FIXME to UUID
  ) => requests.get(`highlights/${pageId}`),
  deleteHighlight: (highlightId: string): Promise<HighlightType> =>
    requests.delete(`highlights/${highlightId}`),
};

// Create an Annotation Object with methods

export const Annotation = {
  createAnnotation: (annotation: AnnotationType): Promise<AnnotationType> =>
    requests.post("/annotations", annotation),
};

// TODO HACK REVIEW
export const getOrgRoamNodes = () => requests.get("/orgRoamNodes");

// export const readOrgFiles = async () => {
//   const res = await axios.get(serverLocation + "orgFiles");
//   return res.data;
// };

// export const getHeadlines = async (filepath) => {
//   const res = await axios.get(
//     serverLocation + "headlines/" + `?filepath=${filepath}`
//   );
//   return res.data;
// };

// export const getOrgRoamNodes = async () => {
//   const res = await axios.get(serverLocation + "orgNodes");
//   return res.data;
// };

// export const getOrgRoamFiles = async () => {
//   const res = await axios.get(serverLocation + "orgRoamFiles");
//   return res.data;
// };
