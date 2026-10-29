# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_36`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Segment 'Action_ComboBlock' for track '19' has invalid range: start=87, end=42. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '22' has invalid range: start=172, end=145. Clamping end to start.
> - Action 'Action_PreSnap' range [0-195] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-221] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-237] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-256] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-282] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-310] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-328] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-218] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-24] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-238] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-274] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-244] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-289] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-265] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-285] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-306] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-323] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-328] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-213] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-272] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-286] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-293] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-86] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-220] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-314] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-276] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 173, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [173-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-262] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-327] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-328] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-261] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-238] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-328] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-291] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-307] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-327] for track '30' has 2 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.