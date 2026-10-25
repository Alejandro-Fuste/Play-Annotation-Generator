# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_89`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_RunBlock' annotated_start=69, effective_Action_RunBlock_start=79.
> - Action 'Action_None' range [64-160] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-226] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-253] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-163] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-195] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-160] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-240] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [69-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [178-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-230] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-148] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-212] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-285] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [69-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-296] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-297] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [79-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [98-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-63] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-137] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-108] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-269] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-240] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-254] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-249] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-299] for track '27' has 4 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.