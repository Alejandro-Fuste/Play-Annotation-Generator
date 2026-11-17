# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_164`
- **Input XML**: `outputs/batch/Power/Power/Power_164/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 330: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 330: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 330: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [30-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-329] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-276] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-307] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-36] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-291] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-207] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-279] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-266] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-233] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-288] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-193] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-60] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [192-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [217-219] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [181-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [199-204] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-241] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-250] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-329] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-236] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-262] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-254] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-290] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-319] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-242] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-277] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-288] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-310] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-255] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-309] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-306] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-312] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-326] for track '31' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.