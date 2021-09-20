export interface HighlightType {
  id: string;
  textBefore: string;
  text: string;
  originalText: string;
  textAfter: string;
  pageId: string; // FIXME set this to UUID
}

export interface AnnotationType {
  id: string; // FIXME
  orgNodeId?: string; // FIXME
  highlightId: string; // FIXME
  pageId: string; // FIXME
  text: string;
}

export interface PageType {
  id: string; // FIXME
  url: string; //FIXME
  title: string;
}
