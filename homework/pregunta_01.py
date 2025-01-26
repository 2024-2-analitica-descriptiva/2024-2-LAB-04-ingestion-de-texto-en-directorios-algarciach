# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import pandas as pd

    if not os.path.exists("./files/output"):
        os.makedirs("./files/output")

    sentiments = ["positive", "negative", "neutral"]

    def load_train_data():
        train_data = []

        for sentiment in sentiments:
            my_path = f"./files/input/train/{sentiment}/"
            for file in os.listdir(my_path):                
                phrase_df = pd.read_csv(os.path.join(my_path, file), names=["phrase"])
                phrase_df["target"] = sentiment
                train_data.append(phrase_df)

        train_df = pd.concat(train_data, ignore_index=True)
        return train_df

    def load_test_data():
        test_data = []

        for sentiment in sentiments:
            my_path = f"./files/input/test/{sentiment}/"
            for file in os.listdir(my_path):                
                phrase_df = pd.read_csv(os.path.join(my_path, file), names=["phrase"])
                phrase_df["target"] = sentiment
                test_data.append(phrase_df)

        test_df = pd.concat(test_data, ignore_index=True)
        return test_df

    def create_train_dataset(df):
        df.to_csv("./files/output/train_dataset.csv")
        
    def create_test_dataset(df):
        df.to_csv("./files/output/test_dataset.csv")


    def main():
        train_df = load_train_data()
        test_df = load_test_data()
        create_train_dataset(train_df)
        create_test_dataset(test_df)

    return main()

if __name__ == '__main__':
    pregunta_01()
