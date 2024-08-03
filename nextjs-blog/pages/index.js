import Head from "next/head";
import { useState } from "react";
import styles from "../styles/Home.module.css";

export default function Home() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [entryValue, setEntryValue] = useState('');

  const handleBoxClick = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  const handleEntryChange = (event) => {
    setEntryValue(event.target.value);
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div
        className={styles.box}
        onClick={handleBoxClick}
        data-testid="click-me"
      >
        Click Me
      </div>

      {entryValue && <h1 data-testid="message">{entryValue}</h1>}

      {isModalOpen && (
        <div className={styles.modal}>
          <div className={styles.modalContent}>
            <span className={styles.close} onClick={handleCloseModal}>
              &times;
            </span>
            <p data-testid="greetings">Hello World</p>
            <input
              type="text"
              data-testid="entry-box"
              placeholder="Enter text here"
              value={entryValue}
              onChange={handleEntryChange}
            />
            <button onClick={handleCloseModal} data-testid="close-modal">
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
