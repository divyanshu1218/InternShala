import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ActivityIndicator, Alert, Platform, TouchableOpacity } from 'react-native';
import { WebView } from 'react-native-webview'; // Requires installation
import { videoService } from '../services/videoService';

export default function VideoPlayerScreen({ route, navigation }) {
    const { videoId, playbackToken, title, description } = route.params;
    const [streamUrl, setStreamUrl] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchStreamUrl();
    }, []);

    const fetchStreamUrl = async () => {
        try {
            const data = await videoService.getStreamUrl(videoId, playbackToken);
            setStreamUrl(data.stream_url);
        } catch (error) {
            Alert.alert('Error', 'Failed to load video stream');
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <View style={styles.centered}>
                <ActivityIndicator size="large" />
            </View>
        );
    }

    return (
        <View style={styles.container}>
            <TouchableOpacity onPress={() => navigation.goBack()} style={styles.backButton}>
                <Text style={styles.backButtonText}>← Back</Text>
            </TouchableOpacity>

            {streamUrl ? (
                <View style={styles.videoContainer}>
                    {Platform.OS === 'web' ? (
                        <iframe
                            src={streamUrl}
                            style={{ width: '100%', height: '100%', border: 'none' }}
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowFullScreen
                        />
                    ) : (
                        <WebView
                            source={{ uri: streamUrl }}
                            style={styles.webview}
                            javaScriptEnabled={true}
                            domStorageEnabled={true}
                            allowsFullscreenVideo={true}
                        />
                    )}
                </View>
            ) : (
                <View style={styles.centered}>
                    <Text>Video unavailable</Text>
                </View>
            )}
            <View style={styles.infoContainer}>
                <Text style={styles.title}>{title}</Text>
                <Text style={styles.description}>{description}</Text>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#000',
    },
    centered: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    videoContainer: {
        height: 250,
        width: '100%',
    },
    webview: {
        flex: 1,
    },
    infoContainer: {
        padding: 20,
    },
    title: {
        color: '#fff',
        fontSize: 22,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    description: {
        color: '#ccc',
        fontSize: 16,
    },
    backButton: {
        padding: 15,
        backgroundColor: '#000',
    },
    backButtonText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
    },
});
