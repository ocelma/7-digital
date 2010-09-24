import py7digital

#Search artist
results = py7digital.search_artist('stones')
print results.get_total_result_count()
for artist in results.get_next_page():
    print artist.get_name() #, artist.get_image(), artist.get_url(), artist.get_tags()
    print '\tTop tracks:'
    for top_track in artist.get_top_tracks():
        print '\t\t', top_track.get_title(), top_track.get_isrc(), top_track.get_duration(), top_track.get_position(), top_track.get_explicit(), top_track.get_version()
    print '\tRec. Albums:'
    for rec_album in artist.get_recommended_albums():
        print '\t\t', rec_album, rec_album.get_year() #, album.get_barcode(), album.get_type(), album.get_artist(), album.get_tags(), album.get_label()
    for album in artist.get_albums(5):
        print '\t', album, album.get_year(), album.get_barcode(), album.get_type(), album.get_artist(), album.get_tags(), album.get_label(), album.get_release_date(), album.get_added_date()
        for sim_album in album.get_similar():
            print '\t\tSimilar:', sim_album, sim_album.get_year(), sim_album.get_artist()
        for track in album.get_tracks():
            print '\t\t', track, track.get_isrc() #, track.get_url(), track.get_audio()

#Browse artists starting with 'J'
results = py7digital.browse_artists('j')
print results.get_total_result_count()
for artist in results.get_next_page():
    print artist.get_name() #, artist.get_image(), artist.get_url(), artist.get_tags()
    for album in artist.get_albums(2):
        print '\t', album, album.get_year() #album.get_barcode(), album.get_type(), album.get_artist(), album.get_tags(), album.get_label()
        for track in album.get_tracks():
            print '\t\t', track.get_title(), track.get_isrc() #, track.get_url(), track.get_audio()

#Search albums
searcher = py7digital.search_album('u2')
print searcher.get_total_result_count()
while searcher.has_results():
    for album in searcher.get_next_page():
        print album, album.get_similar()

#Search tracks
searcher = py7digital.search_track('u2 one')
print searcher.get_total_result_count()
while searcher.has_results():
    for track in searcher.get_next_page():
        print track

# New releases in a given period of time
results = py7digital.album_releases('20100901', '20100924')
for album in results.get_next_page():
    print album, album.get_year(), album.get_barcode(), album.get_type(), album.get_artist(), album.get_tags(), album.get_label(), album.get_release_date(), album.get_added_date()
    for sim_album in album.get_similar():
        print '\tSimilar:', sim_album, sim_album.get_year(), sim_album.get_artist()
    for track in album.get_tracks():
        print '\t', track, track.get_isrc() #, track.get_url(), track.get_audio()

# Album charts in a given period of time
results = py7digital.album_charts('month', '20100901')
for album in results.get_next_page():
    print album, album.get_year(), album.get_barcode(), album.get_type(), album.get_artist(), album.get_tags(), album.get_label(), album.get_release_date(), album.get_added_date()
    for sim_album in album.get_similar():
        print '\tSimilar:', sim_album, sim_album.get_year(), sim_album.get_artist()
    for track in album.get_tracks():
        print '\t', track, track.get_isrc() #, track.get_url(), track.get_audio()

