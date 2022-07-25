import React from "react";
import BarLoader from "react-spinners/BarLoader";

function Loading() {
  return (
    <div class="contentWrap">
        <BarLoader
          color="#2F2E6F"
          height={4}
          width={380}
        />
      </div>
  );
}

export default Loading;