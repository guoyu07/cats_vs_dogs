"""Provides interface for meta-functions that help serve the model."""

import os
import shutil

import tensorflow as tf


def restore_protobuf(session, tag, savedir='saved_protobuf'):
    """
    Restores the model to the session of choice.

    # Parameters
        session (tf.Session): Session to restore to.
        tag (str): An ID for the model.
        savedir (str): Name of the save-dir.
    """
    tf.saved_model.loader.load(session, [tag], savedir)


def save_protobuf(session, tag, savedir='saved_protobuf'):
    """
    Saves the model to a directory.

    # Parameters
        session (tf.Session): A session to save.
        tag (str): An ID for the model.
        savedir (str): Name of the save-dir.
    """
    if savedir in os.listdir():
        shutil.rmtree(savedir)
    saver = tf.saved_model.builder.SavedModelBuilder(savedir)
    saver.add_meta_graph_and_variables(session, [tag])
    saver.save()
