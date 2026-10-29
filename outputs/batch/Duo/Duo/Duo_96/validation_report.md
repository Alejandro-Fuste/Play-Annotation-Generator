# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_96`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_96/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 194: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Segment 'Action_ComboBlock' for track '11' has invalid range: start=237, end=73. Clamping end to start.
> - Action 'Action_PreSnap' range [0-305] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-357] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-284] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-358] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-357] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [237-275] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [278-280] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-358] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-172] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-249] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [237-248] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [256-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-341] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-250] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-257] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-121] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-186] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-242] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-358] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-255] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [312-358] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-236] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '16' starts at frame 237, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [237-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [247-266] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-115] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-220] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-232] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-312] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-255] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [256-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [260-311] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-327] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-300] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-328] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-358] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-315] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-340] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-330] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-341] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-350] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '28' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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