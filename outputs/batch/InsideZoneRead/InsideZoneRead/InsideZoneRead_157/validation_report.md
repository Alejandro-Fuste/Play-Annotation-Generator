# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_157`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_157/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '1' has invalid range: start=327, end=261. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '3' has invalid range: start=327, end=285. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '5' has invalid range: start=327, end=299. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=327, end=299. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '10' has invalid range: start=324, end=299. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '10' has invalid range: start=343, end=299. Clamping end to start.
> - Segment 'Action_BallCarry' for track '10' has invalid range: start=362, end=299. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '12' has invalid range: start=327, end=286. Clamping end to start.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=324, end=279. Clamping end to start.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-276] for track '3' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-285] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-296] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-218] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-274] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-286] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-221] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-276] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-278] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-262] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-292] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-297] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '24' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Action event 'Action_BallSnap' has invalid start frame 324. Video range is [0, 299].
> - Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
> - Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
> - Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
> - Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
> - Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
> - Action event 'Action_SnapReceive' has invalid start frame 337. Video range is [0, 299].
> - Action event 'Action_ReadDefender' has invalid start frame 343. Video range is [0, 299].
> - Action event 'Action_BallCarry' has invalid start frame 362. Video range is [0, 299].
> - Action event 'Action_None' has invalid start frame 391. Video range is [0, 299].
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_157'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.