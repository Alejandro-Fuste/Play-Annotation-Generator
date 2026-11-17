# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_88`
- **Input XML**: `outputs/batch/Power/Power/Power_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 178: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [22-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-345] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-356] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-262] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-231] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-259] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-268] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-235] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-244] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-200] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-251] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [163-194] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-232] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-341] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-356] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-359] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-279] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-326] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-356] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.