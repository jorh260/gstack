{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "13oi0mP01PpjoOmq8nc0WVT_yHquiqQi_",
      "authorship_tag": "ABX9TyNbUtaAxFtguuU7hn4KJSu4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jorh260/gstack/blob/main/exception.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "fWUF-3RH3nyn",
        "outputId": "5fae29b4-d6d4-4013-87f9-721cc4827bb9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        }
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (938560586.py, line 23)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_771/938560586.py\"\u001b[0;36m, line \u001b[0;32m23\u001b[0m\n\u001b[0;31m    super().__init__(f\"Student not found: {student}\")p\u001b[0m\n\u001b[0m                                                     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ],
      "source": [
        "# we are creating exception errors for the big project name score predict data engine.\n",
        "\n",
        "from abc import ABC, abstractmethod\n",
        "\n",
        "class DataError(Exception):\n",
        "   def __init__(self, error_message):\n",
        "    super().__init__(error_message)\n",
        "    self.error_message = error_message\n",
        "\n",
        "   def __str__(self):\n",
        "    return f\"A data-related error occurred: {self.error_message}\"\n",
        "\n",
        "\n",
        "class InvalidScoreError(DataError):\n",
        " def __init__(self, score):\n",
        "  self.score = score\n",
        "  super().__init__(f\"Invalid score entered: {score}\")\n",
        "\n",
        "\n",
        "class StudentNotFoundError(DataError):\n",
        "  def __init__(self, student):\n",
        "     self.student = student\n",
        "     super().__init__(f\"Student not found: {student}\")p\n",
        "\n",
        "\n",
        "class FileLoadError(DataError):\n",
        " def __init__(self, file):\n",
        "     self.file =file\n",
        "     super().__init__(f\"file not found: {file}\")"
      ]
    }
  ]
}