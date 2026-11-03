# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_5`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [6–20], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=21.
> - Action 'Action_RunPostRoute' range [23-156] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-189] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-91] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-47] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [200-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [205-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-58] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-68] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-196] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-206] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-166] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-121] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-164] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '34' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.