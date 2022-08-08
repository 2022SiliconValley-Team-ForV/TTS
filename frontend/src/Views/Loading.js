import React from "react";
import BarLoader from "react-spinners/BarLoader";

function Loading() {
  return (
    <div class="contentWrap">
        <BarLoader 
          color="#2F2E6F"
          height={5}
          width={600}
        />
      </div>
  );
}

export default Loading;