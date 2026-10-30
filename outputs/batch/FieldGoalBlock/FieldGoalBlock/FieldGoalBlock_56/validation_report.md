# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_56`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [212-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-293] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [212-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-298] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-295] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-200] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-258] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-292] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-211] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-262] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-294] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-132] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-137] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-278] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-246] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-278] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-274] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-252] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-274] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-266] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '27' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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