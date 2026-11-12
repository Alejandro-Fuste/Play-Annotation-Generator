# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_211`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_211/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=149, end=145. Clamping end to start.
> - Action 'Action_None' range [146-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-250] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-234] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-263] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-329] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-287] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-217] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-250] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-206] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-208] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-191] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-244] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-212] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [214-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-266] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-211] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-251] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-292] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-196] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-292] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-281] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-295] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-176] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [187-194] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [204-206] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [146-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-328] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [241-318] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-264] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-256] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-264] for track '29' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.