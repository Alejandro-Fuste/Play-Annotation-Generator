# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_58`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 118: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-240] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-274] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-268] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-276] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-251] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-255] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-315] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [135-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-319] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-17] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-329] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-11] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-33] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-188] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-272] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-304] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-313] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-327] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-283] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-288] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-296] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-323] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-316] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-310] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-315] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.