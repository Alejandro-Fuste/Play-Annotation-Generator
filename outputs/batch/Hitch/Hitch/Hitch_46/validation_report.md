# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_46`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [1–25], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=26.
> - Action 'Action_None' range [1-239] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-93] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-92] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-146] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-48] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-61] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [79-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-125] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [1-182] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-180] for track '14' has 8 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [187-204] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [211-212] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-49] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-102] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-93] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-178] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-135] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-178] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.