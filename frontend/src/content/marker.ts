import { Marker } from "@notelix/web-marker";

export const createMarker = () => {
  const marker = new Marker({
    rootElement: document.body,
    eventHandler: {
      onHighlightClick: (context, element) => {
        marker.unpaint(context.serializedRange);
      },
      onHighlightHoverStateChange: (context, element, hovering) => {
        if (hovering) {
          element.style.backgroundColor = "#f0d8ff";
        } else {
          element.style.backgroundColor = "";
        }
      },
    },
    highlightPainter: {
      paintHighlight: (context, element) => {
        // element.style.color = "red";
        element.style.textDecoration = "underline";
        element.style.textDecorationColor = "red";
        element.style["text-decoration-thickness"] = "1px";
      },
    },
  });
  return marker;
};
