# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_123`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_123/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 248: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [292–307], lower_priority='Action_DownBlock' annotated_start=300, effective_Action_DownBlock_start=308.
> - Action 'Action_None' range [292-527] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [333-465] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [467-469] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [476-477] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [484-486] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [490-491] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-413] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-446] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [300-336] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-363] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [308-321] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-489] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-517] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-524] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-499] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-346] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-360] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-454] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-502] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-325] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-335] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-346] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-371] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-509] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-432] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [300-331] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [342-343] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-361] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [363-463] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-485] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-437] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-482] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-362] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-384] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-456] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-408] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-454] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [456-479] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [491-494] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-502] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-518] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-525] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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