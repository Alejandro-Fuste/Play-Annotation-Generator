# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_67`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [38–51], lower_priority='Action_DownBlock' annotated_start=41, effective_Action_DownBlock_start=52.
> - Action 'Action_None' range [38-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-200] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-75] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-210] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [46-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [94-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [82-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-106] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-129] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-155] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '32' has 1 frames without a visible bounding box.
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