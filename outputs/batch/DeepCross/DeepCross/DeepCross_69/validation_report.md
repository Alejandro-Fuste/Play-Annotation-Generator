# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_69`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 72: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 72: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 72: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [16–30], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=31.
> - Action 'Action_None' range [16-133] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-156] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [30-186] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [195-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [205-213] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [222-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-228] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-156] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-175] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-125] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-174] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-123] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [126-156] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [158-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-57] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [62-122] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-153] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-216] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '33' has 3 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.