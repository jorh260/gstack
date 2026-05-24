{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "13oi0mP01PpjoOmq8nc0WVT_yHquiqQi_",
      "authorship_tag": "ABX9TyO3RGwHl71n6tQzrffXSP2c",
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
      "execution_count": 2,
      "metadata": {
        "id": "fWUF-3RH3nyn"
      },
      "outputs": [],
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
        "     super().__init__(f\"Student not found: {student}\")\n",
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